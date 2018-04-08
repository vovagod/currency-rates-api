# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-07 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratesdata',
            name='czk',
            field=models.DecimalField(decimal_places=2, default='10', max_digits=3, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='ratesdata',
            name='eur',
            field=models.DecimalField(decimal_places=2, default='10', max_digits=3, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='ratesdata',
            name='pln',
            field=models.DecimalField(decimal_places=2, default='10', max_digits=3, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='ratesdata',
            name='usd',
            field=models.DecimalField(decimal_places=2, default='10', max_digits=3, verbose_name='Цена'),
        ),
    ]
