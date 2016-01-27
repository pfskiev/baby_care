# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0002_auto_20160126_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=300)),
                ('date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
