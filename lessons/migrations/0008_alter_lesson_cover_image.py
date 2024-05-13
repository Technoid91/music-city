# Generated by Django 3.2.25 on 2024-05-13 21:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0007_alter_subscription_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='cover_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
