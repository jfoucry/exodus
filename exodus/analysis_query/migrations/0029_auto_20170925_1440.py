# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_query', '0028_auto_20170925_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisrequest',
            name='storage_path',
            field=models.TextField(default='apks/5d190774-28b9-435f-97bd-df74af542a24'),
        ),
    ]
