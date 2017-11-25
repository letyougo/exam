# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_client', '0004_labour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labour',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='labour',
            name='teacher',
        ),
        migrations.AddField(
            model_name='exam',
            name='shui',
            field=models.CharField(max_length=128, null=True, verbose_name='税收', blank=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='total',
            field=models.CharField(max_length=128, null=True, verbose_name='总计', blank=True),
        ),
        migrations.DeleteModel(
            name='Labour',
        ),
    ]
