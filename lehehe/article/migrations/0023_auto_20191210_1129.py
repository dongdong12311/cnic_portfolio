# Generated by Django 2.2.8 on 2019-12-10 03:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0022_auto_20191210_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myalgopost',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='myalgopost',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
