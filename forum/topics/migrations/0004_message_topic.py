# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0003_remove_message_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='topic',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='topics.Topic'),
            preserve_default=False,
        ),
    ]
