# Generated by Django 2.2.7 on 2019-11-22 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0004_auto_20191121_0746'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlgoColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column', models.CharField(max_length=200)),
                ('created', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='algo_column', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyalgoPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=500)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('initial_capital', models.CharField(max_length=20)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('portfolio', models.TextField()),
                ('benchmark', models.CharField(max_length=10)),
                ('balanced_dates', models.CharField(max_length=30)),
                ('expected_return_days', models.CharField(max_length=30)),
                ('cov_method', models.CharField(max_length=20)),
                ('beta', models.CharField(max_length=30)),
                ('opt_criterion', models.CharField(max_length=30)),
                ('target_risk', models.CharField(max_length=30)),
                ('p_matrix', models.TextField()),
                ('q_matrix', models.TextField()),
                ('algo_column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='algo_column', to='article.AlgoColumn')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='algo', to=settings.AUTH_USER_MODEL)),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='algo_type_column', to='article.ArticleColumn')),
            ],
            options={
                'ordering': ('-updated',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
