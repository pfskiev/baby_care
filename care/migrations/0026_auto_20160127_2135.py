# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0025_auto_20160127_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='page',
        ),
        migrations.AddField(
            model_name='about',
            name='page',
            field=models.ManyToManyField(blank=True, null=True, to='care.Pages'),
        ),
    ]
