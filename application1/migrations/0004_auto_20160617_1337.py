# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application1', '0003_auto_20160615_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='borrado',
            field=models.CharField(default='1', max_length=1),
        ),
    ]
