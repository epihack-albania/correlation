# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 21:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_reporter', '0009_auto_20160420_2341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='humancase',
            old_name='residency_village',
            new_name='village',
        ),
        migrations.RemoveField(
            model_name='humancase',
            name='residency_commune',
        ),
    ]