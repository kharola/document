# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-19 05:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files_sys', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filesys',
            name='uploaded_by',
        ),
    ]
