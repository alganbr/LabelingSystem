# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-21 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0001_initial'),
        ('profile', '0002_auto_20170720_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='quiz_response_list',
            field=models.ManyToManyField(blank=True, related_name='quiz_response_list', to='response.QuizResponse', verbose_name='quiz_response_list'),
        ),
    ]
