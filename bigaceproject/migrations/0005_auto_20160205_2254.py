# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 22:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bigaceproject', '0004_auto_20160205_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=264, verbose_name='Project Name'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rating_from', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_to', to=settings.AUTH_USER_MODEL, verbose_name='Rated person'),
        ),
    ]
