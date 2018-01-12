# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-12 07:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SDb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True, verbose_name='Название')),
                ('connect', models.CharField(max_length=255, null=True, verbose_name='Строка подключения')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Коментарий')),
                ('checked', models.BooleanField(default=True, verbose_name='Вкл.')),
            ],
            options={
                'verbose_name': 'БД',
                'verbose_name_plural': 'БД',
                'db_table': 'service_db',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(null=True, verbose_name='Информация')),
                ('dt', models.DateTimeField(null=True, verbose_name='Дата и время')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Лог',
                'db_table': 'service_log',
                'ordering': ['-dt'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Содержание')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
                'db_table': 'service_page',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True, verbose_name='Название')),
                ('script', models.TextField(null=True, verbose_name='SQL')),
                ('priority', models.IntegerField(null=True, verbose_name='Приоритет')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('result', models.CharField(blank=True, max_length=255, null=True, verbose_name='Значение ответа')),
            ],
            options={
                'verbose_name': 'Запрос',
                'verbose_name_plural': 'Запросы',
                'db_table': 'service_query',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True, verbose_name='Название')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('checked', models.BooleanField(default=True, verbose_name='Вкл.')),
            ],
            options={
                'verbose_name': 'Сервис',
                'verbose_name_plural': 'Сервисы',
                'db_table': 'service_service',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SServiceDb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_db', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='service.SDb', verbose_name='БД')),
                ('s_service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='service.SService', verbose_name='Сервис')),
            ],
            options={
                'verbose_name': 'Сервис <=> БД',
                'verbose_name_plural': 'Сервисы <=> БД',
                'db_table': 'service_service_db',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип обработки запросов',
                'verbose_name_plural': 'Типы обработки запросов',
                'db_table': 'service_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SUserService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='service.SService', verbose_name='Сервис')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пользователь <=> Сервис',
                'verbose_name_plural': 'Пользователи <=> Сервисы',
                'db_table': 'service_user_service',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='squery',
            name='s_service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='service.SService', verbose_name='Принадлежность к сервису'),
        ),
        migrations.AddField(
            model_name='squery',
            name='s_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='service.SType', verbose_name='Тип обработки запроса'),
        ),
    ]
