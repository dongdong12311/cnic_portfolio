# Generated by Django 2.2.8 on 2019-12-09 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0019_remove_algoopt_task_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algoopt',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='algooptuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
