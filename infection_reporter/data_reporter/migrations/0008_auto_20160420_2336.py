# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 21:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_reporter', '0007_auto_20160420_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalcase',
            name='disease',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='data_reporter.Disease'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='disease',
            name='animal',
            field=models.BooleanField(default=False, verbose_name='Animal'),
        ),
        migrations.AddField(
            model_name='disease',
            name='human',
            field=models.BooleanField(default=False, verbose_name='Human'),
        ),
        migrations.AddField(
            model_name='disease',
            name='sequela',
            field=models.BooleanField(default=False, verbose_name='Sequela'),
        ),
    ]