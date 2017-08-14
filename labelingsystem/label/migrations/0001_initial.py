# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 02:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000, verbose_name='content')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post', verbose_name='post')),
            ],
            options={
                'verbose_name': 'label',
                'verbose_name_plural': 'labels',
            },
        ),
    ]