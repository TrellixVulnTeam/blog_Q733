# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-22 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190822_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content_img',
            field=models.ImageField(upload_to='md/img'),
        ),
        migrations.AlterField(
            model_name='article',
            name='file',
            field=models.FileField(upload_to='md/file'),
        ),
    ]
