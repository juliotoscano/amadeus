# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

    def __str__(self):
        return self.name

class Modules(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    description = models.TextField('Descrição', blank=True)
    material = models.FileField('Material',upload_to='materials_course/', null=True, blank=True)
    activities = models.FileField('Atividades',upload_to='activities_course/', null=True, blank=True)
    is_visible = models.BooleanField(
        'Visível', default=False, blank=True
        )

    class Meta:
        verbose_name = 'Modulo'
        verbose_name_plural = 'Modulos'

    def __str__(self):
        return self.name

# Função para atualização de imagens
def upload_location(instance, filename):
    return"%s/%s" %(instance.id, filename)

class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    description = models.TextField('Descrição', blank=True)
    program = models.TextField('Programação', blank=True)
    qtd_available = models.IntegerField('Vagas')
    qtd_students = models.IntegerField('Alunos_matriculados')
    begin_matric = models.DateField('Inicio_inscrições', null=True, blank=True)
    end_matric = models.DateField('Fim_inscrições', null=True, blank=True)
    begin_course = models.DateField('Inicio_curso',  null=True, blank=True)
    end_course = models.DateField('Fim_curso',  null=True, blank=True)
    image = models.ImageField('Foto', upload_to=upload_location, null=True, blank=True)
    is_approved = models.BooleanField(
        'Aprovado', default=False, blank=True
        )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='courses',
        verbose_name='professor'
        )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='courses',
        verbose_name = 'categoria'
        )
    modules = models.ForeignKey(
        Modules,
        on_delete=models.CASCADE,
        related_name='courses',
        blank=True,
        default=True,
        verbose_name='Modulos'
        )
    keywords =models.CharField('Palavras_chave', max_length=100, blank=True)

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'

    def __str__(self):
        return self.name

