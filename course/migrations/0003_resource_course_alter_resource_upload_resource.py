# Generated by Django 4.1.8 on 2024-01-12 10:43

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_coursepage_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='course',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_resource', to='course.coursepage'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='upload_resource',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
