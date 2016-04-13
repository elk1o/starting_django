# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoria', models.CharField(max_length=25)),
                ('borrado', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Espectaculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('espectaculo', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('hora', models.DateTimeField()),
                ('descripcion', models.CharField(max_length=255)),
                ('recaudacion', models.DecimalField(max_digits=10, decimal_places=2)),
                ('vendidas', models.IntegerField()),
                ('imagen', models.CharField(max_length=255)),
                ('aforo_completo', models.BooleanField()),
                ('categoria', models.ForeignKey(to='application1.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lugar', models.CharField(max_length=25)),
                ('borrado', models.CharField(max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='espectaculo',
            name='lugar',
            field=models.ForeignKey(to='application1.Lugar'),
        ),
    ]
