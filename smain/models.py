# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

class SDb(models.Model):
    name = models.CharField(unique=True, max_length=100, null=True, verbose_name='Название')
    p_host = models.CharField(max_length=255, null=True, verbose_name='Сервер')
    p_name = models.CharField(max_length=255, null=True, verbose_name='БД')
    p_username = models.CharField(max_length=100, null=True, verbose_name='Пользователь')
    p_password = models.CharField(max_length=100, null=True, verbose_name='Пароль')
    comment = models.TextField(blank=True, null=True, verbose_name='Коментарий')
    checked = models.BooleanField(blank=True, verbose_name='Вкл.')

    class Meta:
        managed = False
        db_table = 's_db'
        verbose_name = 'БД'
        verbose_name_plural = 'БД'

    def __str__(self):
        return self.name 


class SAuthUserDb(models.Model):
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING, null=True, verbose_name='Пользователь')
    s_db = models.ForeignKey('SDb', models.DO_NOTHING, null=True, verbose_name='БД')

    class Meta:
        managed = False
        db_table = 's_auth_user_db'
        verbose_name = 'Пользователь <=> БД'
        verbose_name_plural = 'Пользователи <=> БД'

    def __str__(self):
        return '{0.auth_user} <=> {0.s_db}'.format(self)


class SAuthUserService(models.Model):
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING, null=True, verbose_name='Пользователь')
    s_service = models.ForeignKey('SService', models.DO_NOTHING, null=True, verbose_name='Сервис')    

    class Meta:
        managed = False
        db_table = 's_auth_user_service'
        verbose_name = 'Пользователь <=> Сервис'
        verbose_name_plural = 'Пользователи <=> Сервисы'


class SLog(models.Model):
    info = models.TextField(null=True, verbose_name='Информация')
    dt = models.DateTimeField(null=True, verbose_name='Дата и время')

    class Meta:
        managed = False
        db_table = 's_log'
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
        managed = False
        db_table = 's_query'
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    def __str__(self):
        return self.name


class SService(models.Model):
    name = models.CharField(unique=True, max_length=100, null=True, verbose_name='Название')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    checked = models.BooleanField(blank=True, verbose_name='Вкл.')

    class Meta:
        managed = False
        db_table = 's_service'
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'

    def __str__(self):
        return self.name


class SType(models.Model):
    name = models.CharField(unique=True, max_length=255, null=True, verbose_name='Название')    

    class Meta:
        managed = False
        db_table = 's_type'
        verbose_name = 'Тип обработки запросов'
        verbose_name_plural = 'Типы обработки запросов'

    def __str__(self):
        return self.name