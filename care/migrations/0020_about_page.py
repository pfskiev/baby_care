# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0019_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='care.Map'),
        ),
    ]
