# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0006_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
            ],
        ),
    ]
