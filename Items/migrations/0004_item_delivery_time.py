# Generated by Django 3.0.5 on 2020-06-23 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0003_auto_20200623_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='delivery_time',
            field=models.IntegerField(default=14),
        ),
    ]
