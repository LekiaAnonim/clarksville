from django.db import models
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel, PageChooserPanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from authentication.models import User
from django.urls import reverse
from authentication.models import MembershipStatus
# from wagtailmetadata.models import MetadataPageMixin
# Create your models here.
class CourseIndexPage(Page):
    template = 'courses/all_courses.html'
    intro = RichTextField(blank=True)
    membership_type = models.ForeignKey(MembershipStatus, null=True, blank=True, on_delete=models.SET_NULL, related_name='member_status')

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('membership_type'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(CourseIndexPage, self).get_context(request, *args, **kwargs)
        all_courses = CoursePage.objects.live()
        completed_lessons = LessonPage.objects.live().filter(users = self.owner)  
        context["all_courses"] = all_courses
        return context

class CoursePage(Page):
    template = 'courses/course_detail.html'
    course_title = models.CharField(max_length=500, null=True)
    course_description = RichTextField(blank=True)
    banner = models.ImageField(null=True)

    content_panels = Page.content_panels + [
        FieldPanel('course_title'),
        FieldPanel('course_description'),
        FieldPanel('banner'),
    ]

    def __str__(self):
        return self.course_title
    
    def get_context(self, request, *args, **kwargs):
        context = super(CoursePage, self).get_context(request, *args, **kwargs)
        
        course_lessons = LessonPage.objects.live().filter(course__course_title = self.course_title)
        member = []
        
        for lesson in course_lessons:
            for user in lesson.users.all():
                if user == request.user:
                    member.append(user)
        if member:
            member_course_completed_lessons = LessonPage.objects.live().filter(course__course_title = self.course_title, users=member[0])
            member_course_uncompleted_lessons = LessonPage.objects.live().filter(course__course_title = self.course_title).exclude(users=member[0])
            resume_page = member_course_uncompleted_lessons.first()
            
        else:
            member_course_completed_lessons = []
            member_course_uncompleted_lessons = LessonPage.objects.live().filter(course__course_title = self.course_title)
            resume_page = member_course_uncompleted_lessons.first()

        lesson_percent_complete = (len(member_course_completed_lessons)/len(course_lessons))*100
        context["course_lessons"] = course_lessons
        context["member_course_completed_lessons"] = member_course_completed_lessons
        context["member_course_uncompleted_lessons"] = member_course_uncompleted_lessons
        context["lesson_percent_complete"] = lesson_percent_complete
        context["resume_page"] = resume_page
        return context
    
class LessonPage(Page):
    template = 'courses/lesson_detail.html'
    lesson_title = models.CharField(max_length=500, null=True)
    course =  ParentalKey('CoursePage', null=True, blank=True, on_delete=models.SET_NULL, related_name='course_lesson')
    date_created = models.DateField(auto_now=True)
    lesson_content = RichTextField(blank=True)
    users = ParentalManyToManyField(User, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('lesson_title'),
        FieldPanel('course'),
        FieldPanel('lesson_content'),
        FieldPanel('users'),
    ]

    def __str__(self):
        return self.lesson_title

    def add_authenticated_user(self, user_id):
        try:
            # Fetch the authenticated user
            authenticated_user = User.objects.get(pk=user_id)
            
            if authenticated_user.is_authenticated:
                if authenticated_user in self.users.all():
                    completed = True
                else:
                    completed = False
                    # Add the authenticated user to the many-to-many field
                    self.users.add(authenticated_user)
                    self.save()
                return completed
        except User.DoesNotExist:
            return False
        
    def get_context(self, request, *args, **kwargs):
        context = super(LessonPage, self).get_context(request, *args, **kwargs)
        
        course_lessons = LessonPage.objects.live().filter(course__course_title = self.course.course_title)
        member = []
        
        for lesson in course_lessons:
            for user in lesson.users.all():
                if user == request.user:
                    member.append(user)
        if member:
            member_course_completed_lessons = LessonPage.objects.live().filter(course__course_title = self.course.course_title, users=member[0])
            member_course_uncompleted_lessons = LessonPage.objects.live().filter(course__course_title = self.course.course_title).exclude(users=member[0])
            resume_page = member_course_uncompleted_lessons.first()
            
        else:
            member_course_completed_lessons = []
            member_course_uncompleted_lessons = LessonPage.objects.live().filter(course__course_title = self.course.course_title)
            resume_page = member_course_uncompleted_lessons.first()

        lesson_percent_complete = (len(member_course_completed_lessons)/len(course_lessons))*100
        context["course_lessons"] = course_lessons
        context["member_course_completed_lessons"] = member_course_completed_lessons
        context["member_course_uncompleted_lessons"] = member_course_uncompleted_lessons
        context["lesson_percent_complete"] = lesson_percent_complete
        context["resume_page"] = resume_page
        return context

    def get_next_url(self):
        self.add_authenticated_user(self.owner.id)
        if self.get_next_sibling():
            next = self.get_next_sibling().url
        else:
            next = reverse('course:course_complete')
        return next


@register_snippet
class Objective(models.Model):
    objective = RichTextField(null=True)
    lesson = ParentalKey('LessonPage', null=True, blank=True, on_delete=models.SET_NULL, related_name='lesson_objective')

    panels = [
        FieldPanel('objective'),
        FieldPanel('lesson'),
    ]
    def __str__(self):
        return self.objective

    class Meta:
        verbose_name_plural = "Objectives"


@register_snippet
class Resource(models.Model):
    resource_title = models.CharField(max_length=500, null=True)
    upload_resource = models.FileField()

    panels = [
        FieldPanel('resource_title'),
        FieldPanel('upload_resource'),
    ]
    def __str__(self):
        return self.resource_title

    class Meta:
        verbose_name_plural = "Resources"
    