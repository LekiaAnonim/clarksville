# Generated by Django 4.2.5 on 2024-01-03 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_homepage_about_church_title_3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importantpages',
            name='course_index',
        ),
    ]
