# Generated by Django 3.0.5 on 2020-06-23 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0004_item_delivery_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
