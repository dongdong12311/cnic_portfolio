# Generated by Django 2.2.7 on 2019-11-23 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20191123_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myalgopost',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='myalgopost',
            name='start_date',
            field=models.DateField(),
        ),
    ]
