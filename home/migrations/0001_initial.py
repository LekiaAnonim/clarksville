# Generated by Django 4.1.8 on 2024-01-03 16:56

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.contrib.forms.models
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('who_we_are', wagtail.fields.RichTextField(blank=True, null=True)),
                ('our_belief', wagtail.fields.RichTextField(blank=True, null=True)),
                ('ministries', wagtail.fields.RichTextField(blank=True, null=True)),
                ('regional_overseer', wagtail.fields.RichTextField(blank=True, null=True)),
                ('general_superintendent', wagtail.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ContactFormPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('to_address', models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, validators=[wagtail.contrib.forms.models.validate_to_address], verbose_name='to address')),
                ('from_address', models.EmailField(blank=True, max_length=255, verbose_name='from address')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
                ('thank_you_text', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.forms.models.FormMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='DailyDevotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devotion_type', models.CharField(blank=True, max_length=500, null=True)),
                ('devotion_url', models.URLField(blank=True, null=True)),
                ('devotion_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('caption_title', wagtail.fields.RichTextField(blank=True, null=True)),
                ('caption_text', wagtail.fields.RichTextField(blank=True, null=True)),
                ('donate_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('hero_section_text', wagtail.fields.RichTextField(blank=True, null=True)),
                ('slider_image_1', models.ImageField(blank=True, null=True, upload_to='')),
                ('slider_image_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('slider_image_3', models.ImageField(blank=True, null=True, upload_to='')),
                ('slider_image_4', models.ImageField(blank=True, null=True, upload_to='')),
                ('slider_image_5', models.ImageField(blank=True, null=True, upload_to='')),
                ('about_church_background_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('about_church_title_1', models.CharField(blank=True, max_length=500, null=True)),
                ('about_church_text_1', wagtail.fields.RichTextField(blank=True, null=True)),
                ('about_church_image_1', models.ImageField(blank=True, null=True, upload_to='')),
                ('about_church_title_2', models.CharField(blank=True, max_length=500, null=True)),
                ('about_church_text_2', wagtail.fields.RichTextField(blank=True, null=True)),
                ('about_church_title_3', models.CharField(blank=True, max_length=500, null=True)),
                ('about_church_text_3', wagtail.fields.RichTextField(blank=True, null=True)),
                ('about_church_title_4', models.CharField(blank=True, max_length=500, null=True)),
                ('about_church_text_4', wagtail.fields.RichTextField(blank=True, null=True)),
                ('about_church_image_4', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SubscribeFormPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('to_address', models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, validators=[wagtail.contrib.forms.models.validate_to_address], verbose_name='to address')),
                ('from_address', models.EmailField(blank=True, max_length=255, verbose_name='from address')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
                ('thank_you_text', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.forms.models.FormMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='WorshipService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_title', models.CharField(blank=True, max_length=500, null=True)),
                ('service_day', models.CharField(blank=True, max_length=500, null=True)),
                ('time_from', models.CharField(blank=True, max_length=500, null=True)),
                ('time_to', models.CharField(blank=True, max_length=500, null=True)),
                ('service_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('join_via_facebook_live_link', models.URLField(blank=True, null=True)),
                ('join_via_youtube_live_link', models.URLField(blank=True, null=True)),
                ('join_via_zoom_live_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubscribeFormSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
                ('subscribe_form_page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubscribeFormField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('clean_name', models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name')),
                ('label', models.CharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.TextField(blank=True, help_text='Comma or new line separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices')),
                ('default_value', models.TextField(blank=True, help_text='Default value. Comma or new line separated values supported for checkboxes.', verbose_name='default value')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='help text')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='home.subscribeformpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiteSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, max_length=500, null=True)),
                ('twitter', models.URLField(blank=True, max_length=500, null=True)),
                ('instagram', models.URLField(blank=True, max_length=500, null=True)),
                ('threads', models.URLField(blank=True, max_length=500, null=True)),
                ('linkedin', models.URLField(blank=True, max_length=500, null=True)),
                ('youtube', models.URLField(blank=True, max_length=500, null=True)),
                ('tiktok', models.URLField(blank=True, max_length=500, null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiteLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiteContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email1', models.EmailField(blank=True, help_text='Your Email address', max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('phone2', models.CharField(blank=True, max_length=500, null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImportantPages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('donate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('home', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactFormSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_form_page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.page')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactFormField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('clean_name', models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name')),
                ('label', models.CharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.TextField(blank=True, help_text='Comma or new line separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices')),
                ('default_value', models.TextField(blank=True, help_text='Default value. Comma or new line separated values supported for checkboxes.', verbose_name='default value')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='help text')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='home.contactformpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
