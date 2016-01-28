# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0027_auto_20160127_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='page',
        ),
        migrations.AddField(
            model_name='about',
            name='page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='care.Pages'),
        ),
    ]
