# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('label', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='content',
            field=models.CharField(default=None, max_length=1000, verbose_name='content'),
        ),
    ]