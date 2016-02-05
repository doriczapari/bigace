# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-05 15:58
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigaceproject', '0002_auto_20160205_1130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technology',
            options={'verbose_name_plural': 'Technologies'},
        ),
        migrations.AddField(
            model_name='technology',
            name='level',
            field=models.SmallIntegerField(blank=True, choices=[(0, 'Novice'), (1, 'Intermediate'), (2, 'Expert')], null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ratings',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.SmallIntegerField(), blank=True, null=True, size=None),
        ),
    ]
