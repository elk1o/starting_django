# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-15 09:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application1', '0002_ticket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lugar',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Lugares'},
        ),
    ]
