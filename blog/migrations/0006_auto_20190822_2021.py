# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-22 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190822_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
