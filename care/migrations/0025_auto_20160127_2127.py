# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 21:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0024_auto_20160127_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='care.Pages'),
        ),
    ]
