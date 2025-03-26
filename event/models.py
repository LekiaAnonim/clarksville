from django.db import models
from wagtail.fields import RichTextField
from wagtail.models import Page
from cloudinary.models import CloudinaryField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from django.shortcuts import render

# Create your models here.
class EventIndexPage(Page):
    template = 'event/outreach_list.html'
    intro = RichTextField(blank=True)
    banner = CloudinaryField("image", null=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('banner')
    ]
    def get_context(self, request, *args, **kwargs):
        context = super(EventIndexPage, self).get_context(request, *args, **kwargs)

        outreaches = EventPage.objects.all()
        
        context["outreaches"] = outreaches
        return context

class EventFormField(AbstractFormField):
    page = ParentalKey('EventPage', on_delete=models.CASCADE, related_name='form_fields')

class EventPage(AbstractEmailForm):
    template = 'event/outreach_page.html'
    event_title = models.CharField(max_length=500, null=True, blank=True)
    short_description = models.CharField(max_length=1000, null=True, blank=True, help_text="Enter a text less than 250 words")
    display_on_home_page = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    event_image = CloudinaryField("image", null=True, blank=True)
    event_body = RichTextField(null=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        MultiFieldPanel([
            FieldPanel('event_title'),
            FieldPanel('short_description'),
            FieldPanel('display_on_home_page'),
            FieldPanel('event_image'),
        ], heading="Post information"),
        FieldPanel('event_body'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def save(self, *args, **kwargs):
        if self.display_on_home_page:
            EventPage.objects.all().update(**{'display_on_home_page': False})
        super(EventPage, self).save(*args, **kwargs)

    def serve(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.get_form(request.POST, page=self, user=request.user)
            if form.is_valid():
                self.process_form_submission(form)
                # Update the original landing page context with other data
                landing_page_context = self.get_context(request)
                landing_page_context['email'] = form.cleaned_data['email_address']
                return render(
                    request,
                    self.get_landing_page_template(request),
                    landing_page_context
                )
        else:
            form = self.get_form(page=self, user=request.user)
        context = self.get_context(request)
        context['form'] = form
        return render(
            request,
            self.get_template(request),
            context
        )
    class Meta:
        ordering = ["-date_created"]