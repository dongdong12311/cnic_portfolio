# Generated by Django 2.2.7 on 2019-11-23 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20191123_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myalgopost',
            name='initial_capital',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
