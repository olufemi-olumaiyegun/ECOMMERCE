# Generated by Django 3.0.5 on 2020-06-24 20:27

import Items.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0007_auto_20200624_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='picture',
        ),
        migrations.AddField(
            model_name='images',
            name='pictures',
            field=models.ImageField(blank=True, null=True, upload_to=Items.models.upload_image_path),
        ),
    ]
