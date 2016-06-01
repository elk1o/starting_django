# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('pin', models.CharField(max_length=50, verbose_name='Pin')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
            ],
        ),
    ]
