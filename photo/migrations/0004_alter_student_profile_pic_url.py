# Generated by Django 3.2 on 2021-04-29 19:46

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_auto_20210427_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic_url',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='django-upload'),
        ),
    ]
