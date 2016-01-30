# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0039_auto_20160128_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='hello',
            field=models.ManyToManyField(blank=True, to='care.Task'),
        ),
    ]
