# Generated by Django 3.0.5 on 2020-06-23 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0002_auto_20200623_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default=5000.5, max_digits=8),
        ),
    ]
