# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-06 10:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(help_text='Enter the question text', max_length=1000, verbose_name='question')),
                ('explanation', models.TextField(blank=True, help_text='Explanation to be shown after the question has been answered', max_length=2000, verbose_name='explanation')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_category', to='category.Category', verbose_name='category')),
                ('creator', models.ForeignKey(help_text='The creator of the quiz', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='creator')),
            ],
            options={
                'ordering': ['category'],
                'verbose_name': 'question',
                'verbose_name_plural': 'questions',
            },
        ),
    ]
