# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 01:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0001_initial'),
        ('label', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coder', models.EmailField(default=None, max_length=254, verbose_name='coder')),
            ],
            options={
                'verbose_name_plural': 'participantions',
                'verbose_name': 'participation',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('creator', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='creator')),
                ('label_list', models.ManyToManyField(blank=True, default=None, to='label.Label', verbose_name='label list')),
                ('post_list', models.ManyToManyField(blank=True, default=None, to='post.Post', verbose_name='post list')),
                ('prerequisite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz', verbose_name='prerequisite')),
            ],
            options={
                'verbose_name_plural': 'tasks',
                'verbose_name': 'task',
            },
        ),
        migrations.AddField(
            model_name='participation',
            name='task',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='task.Task', verbose_name='task'),
        ),
        migrations.AlterUniqueTogether(
            name='participation',
            unique_together=set([('task', 'coder')]),
        ),
    ]
