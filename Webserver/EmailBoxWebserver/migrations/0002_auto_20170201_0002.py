# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-31 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmailBoxWebserver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nachricht',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nachricht_text', models.CharField(max_length=100)),
                ('zeitstempel', models.DateTimeField()),
                ('EmailAddresse', models.EmailField(max_length=254)),
                ('Showen', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='MessageModel',
        ),
    ]
