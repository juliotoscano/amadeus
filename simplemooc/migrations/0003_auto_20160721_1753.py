# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 20:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simplemooc', '0002_auto_20160721_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='simplemooc.Teacher', verbose_name='professor'),
        ),
    ]