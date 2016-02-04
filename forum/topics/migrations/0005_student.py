# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0004_message_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('subj', models.CharField(max_length=5)),
                ('mark', models.IntegerField()),
            ],
        ),
    ]