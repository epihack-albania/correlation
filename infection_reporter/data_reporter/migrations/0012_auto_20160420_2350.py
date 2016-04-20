# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_reporter', '0011_auto_20160420_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='humancase',
            name='confirm_count',
        ),
        migrations.RemoveField(
            model_name='humancase',
            name='end_period',
        ),
        migrations.RemoveField(
            model_name='humancase',
            name='probable_count',
        ),
        migrations.RemoveField(
            model_name='humancase',
            name='severity_level',
        ),
        migrations.RemoveField(
            model_name='humancase',
            name='suspected_count',
        ),
        migrations.AddField(
            model_name='humancase',
            name='attack_rate',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=3, verbose_name='Attack Rate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='humancase',
            name='death_rate',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=3, verbose_name='Death Rate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='humancase',
            name='recovery_rate',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=3, verbose_name='Recovery Rate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='humancase',
            name='sequela_rate',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=3, verbose_name='Sequela Rate'),
            preserve_default=False,
        ),
    ]
