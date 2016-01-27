# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0010_auto_20160127_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=300)),
                ('logo', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
