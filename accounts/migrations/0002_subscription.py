# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 11:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simplemooc', '0005_auto_20160816_0854'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='InscricaoCurso', to='simplemooc.Course', verbose_name='Curso_inscrito')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='InscricaoUsusario', to=settings.AUTH_USER_MODEL, verbose_name='Usuario_inscrito')),
            ],
            options={
                'verbose_name': 'Inscricao',
                'verbose_name_plural': 'Inscricoes',
            },
        ),
    ]
