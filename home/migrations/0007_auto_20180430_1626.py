# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-30 10:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20180430_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionbase',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]