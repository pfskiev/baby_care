# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 14:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('care', '0034_auto_20160128_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
