# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0036_auto_20160128_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
