# Generated by Django 2.2.8 on 2019-12-09 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_auto_20191209_2157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='algoopt',
            old_name='algopost',
            new_name='author',
        ),
    ]