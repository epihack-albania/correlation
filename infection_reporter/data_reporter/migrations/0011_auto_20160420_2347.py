# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_reporter', '0010_auto_20160420_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='humancase',
            name='start_period',
        ),
        migrations.AddField(
            model_name='humancase',
            name='avg_age',
            field=models.DecimalField(decimal_places=1, default=1.0, max_digits=3, verbose_name='Average Age'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='humancase',
            name='max_age',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=3, verbose_name='Max Age'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='humancase',
            name='min_age',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=3, verbose_name='Min. Age'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='humancase',
            name='vaccination_rate',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=3, verbose_name='Vaccination Rate'),
            preserve_default=False,
        ),
    ]
