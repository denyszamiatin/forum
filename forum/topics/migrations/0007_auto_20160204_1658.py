# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 16:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0006_delete_student'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterModelOptions(
            name='moder',
            options={'verbose_name_plural': 'Модераторы'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name_plural': 'Темы'},
        ),
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='message',
            name='rate',
            field=models.IntegerField(verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(verbose_name='Текст сообщения'),
        ),
        migrations.AlterField(
            model_name='message',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.Topic', verbose_name='Тема'),
        ),
    ]
