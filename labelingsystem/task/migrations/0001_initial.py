# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-06 10:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('question', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='title')),
                ('description', models.TextField(blank=True, help_text='a description of the quiz', verbose_name='description')),
                ('random_order', models.BooleanField(default=False, help_text='Display the questions in a random order or as they are set', verbose_name='random_order')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_category', to='category.Category', verbose_name='category')),
                ('creator', models.ForeignKey(help_text='The creator of the quiz', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='creator')),
                ('question_list', models.ManyToManyField(blank=True, default=None, help_text='The questions in the quiz', to='question.Question', verbose_name='question_list')),
            ],
            options={
                'verbose_name': 'task',
                'verbose_name_plural': 'tasks',
            },
        ),
    ]
