# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 06:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20170815_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizresponse',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='quizresponse',
            name='responder',
        ),
        migrations.DeleteModel(
            name='QuizResponse',
        ),
    ]
