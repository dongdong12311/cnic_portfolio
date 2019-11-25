# Generated by Django 2.2.7 on 2019-11-21 02:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('algo_name', models.CharField(max_length=300)),
                ('update_time', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('gp', '股票'), ('zq', '债券'), ('jj', '基金')], default='gp', max_length=10)),
                ('algo_content', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('initial_capital', models.CharField(db_index=True, max_length=20)),
                ('algo_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-update_time',),
            },
        ),
    ]
