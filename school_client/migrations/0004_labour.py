# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_client', '0003_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='Labour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('total', models.CharField(max_length=128, null=True, verbose_name='总计', blank=True)),
                ('shui', models.CharField(max_length=128, null=True, verbose_name='税收', blank=True)),
                ('exam', models.ForeignKey(to='school_client.Exam', verbose_name='考试名称', null=True, blank=True)),
                ('teacher', models.ForeignKey(to='school_client.Teacher', verbose_name='监考老师', null=True)),
            ],
        ),
    ]
