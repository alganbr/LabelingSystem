# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-12 22:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='rquired_quiz',
            new_name='required_quiz',
        ),
    ]
