# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class SDb(models.Model):
    name = models.CharField(unique=True, max_length=100, null=True, verbose_name='Название')
    p_host = models.CharField(max_length=255, null=True, verbose_name='Сервер')
    p_name = models.CharField(max_length=255, null=True, verbose_name='БД')
    p_username = models.CharField(max_length=100, null=True, verbose_name='Пользователь')
    p_password = models.CharField(max_length=100, null=True, verbose_name='Пароль')
    comment = models.TextField(blank=True, null=True, verbose_name='Коментарий')
    checked = models.BooleanField(verbose_name='Вкл.', default=True)

    class Meta:
        managed = True
        db_table = 'service_db'
        verbose_name = 'БД'
        verbose_name_plural = 'БД'

    def __str__(self):
        return self.name 


class SUserDb(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, null=True, verbose_name='Пользователь')
    s_db = models.ForeignKey('SDb', models.DO_NOTHING, null=True, verbose_name='БД')

    class Meta:
        managed = True
        db_table = 'service_user_db'
        verbose_name = 'Пользователь <=> БД'
        verbose_name_plural = 'Пользователи <=> БД'

    def __str__(self):
        return '{0.user} <=> {0.s_db}'.format(self)


class SUserService(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, null=True, verbose_name='Пользователь')
    s_service = models.ForeignKey('SService', models.DO_NOTHING, null=True, verbose_name='Сервис')    

    class Meta:
        managed = True
        db_table = 'service_user_service'
        verbose_name = 'Пользователь <=> Сервис'
        verbose_name_plural = 'Пользователи <=> Сервисы'


class SLog(models.Model):
    info = models.TextField(null=True, verbose_name='Информация')
    dt = models.DateTimeField(null=True, verbose_name='Дата и время')

    class Meta:
        managed = True
        db_table = 'service_log'
        verbose_name = 'Лог'
        verbose_name_plural = 'Лог'
        ordering = ['-dt']

    def __str__(self):
        return self.info 


class SQuery(models.Model):
    name = models.CharField(unique=True, max_length=100, null=True, verbose_name='Название')
    s_service = models.ForeignKey('SService', models.DO_NOTHING, null=True, verbose_name='Принадлежность к сервису')
    script = models.TextField(null=True, verbose_name='SQL')
    priority = models.IntegerField(null=True, verbose_name='Приоритет')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    s_type = models.ForeignKey('SType', models.DO_NOTHING, null=True, verbose_name='Тип обработки запроса')
    result = models.CharField(max_length=255, blank=True, null=True, verbose_name='Значение ответа')

    class Meta:
        managed = True
        db_table = 'service_query'
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    def __str__(self):
        return self.name


class SService(models.Model):
    name = models.CharField(unique=True, max_length=100, null=True, verbose_name='Название')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    checked = models.BooleanField(verbose_name='Вкл.', default=True)

    class Meta:
        managed = True
        db_table = 'service_service'
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'

    def __str__(self):
        return self.name


class SType(models.Model):
    name = models.CharField(unique=True, max_length=255, null=True, verbose_name='Название')    

    class Meta:
        managed = True
        db_table = 'service_type'
        verbose_name = 'Тип обработки запросов'
        verbose_name_plural = 'Типы обработки запросов'

    def __str__(self):
        return self.name

class SPage(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='Название')
    content = models.TextField(blank=True, null=True, verbose_name='Содержание')
    user = models.ForeignKey(User, models.DO_NOTHING, null=True, verbose_name='Пользователь')

    class Meta:
        managed = True
        db_table = 'service_page'
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.name