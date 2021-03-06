# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 01:31
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0001_initial'),
        ('label', '0001_initial'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('label', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='label.Label', verbose_name='label')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='post.Post', verbose_name='post')),
                ('responder', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='responder')),
                ('task', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='task.Task', verbose_name='task')),
            ],
            options={
                'verbose_name_plural': 'post responses',
                'verbose_name': 'post response',
            },
        ),
        migrations.CreateModel(
            name='QuizResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz', verbose_name='quiz')),
                ('responder', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='responder')),
            ],
            options={
                'verbose_name_plural': 'quiz responses',
                'verbose_name': 'quiz response',
            },
        ),
    ]
