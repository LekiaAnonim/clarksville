# Generated by Django 4.1.8 on 2024-01-08 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_dailydevotion_devotion_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='hero_section_title',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
