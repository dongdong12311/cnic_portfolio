# Generated by Django 2.2.7 on 2019-12-03 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_myalgopost_target_return'),
    ]

    operations = [
        migrations.AddField(
            model_name='myalgopost',
            name='algo_code',
            field=models.TextField(blank=True),
        ),
    ]