# Generated by Django 2.2.7 on 2019-11-23 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20191123_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myalgopost',
            name='beta',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='myalgopost',
            name='cov_method',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='myalgopost',
            name='expected_return_days',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='myalgopost',
            name='initial_capital',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='myalgopost',
            name='opt_criterion',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='myalgopost',
            name='p_matrix',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='myalgopost',
            name='q_matrix',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='myalgopost',
            name='target_risk',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
