# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-28 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('bday', models.DateField()),
            ],
        ),
    ]
