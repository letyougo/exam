# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_client', '0002_auto_20171124_1230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='教师姓名', max_length=128, null=True, blank=True)),
                ('place', models.CharField(verbose_name='考试地点', max_length=256, null=True, blank=True)),
                ('start', models.DateTimeField(verbose_name='开始时间', null=True, blank=True)),
                ('end', models.DateTimeField(verbose_name='结束时间', null=True, blank=True)),
                ('teacher', models.ManyToManyField(verbose_name='监考老师', to='school_client.Teacher')),
            ],
            options={
                'verbose_name': '考试',
                'verbose_name_plural': '考试',
            },
        ),
    ]
