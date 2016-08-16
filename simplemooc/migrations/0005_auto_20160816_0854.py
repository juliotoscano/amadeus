# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplemooc', '0004_course_modules'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='Identify'),
        ),
    ]