# Generated by Django 3.0.5 on 2020-06-23 07:30

import Items.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0005_item_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=Items.models.upload_image_path),
        ),
    ]
