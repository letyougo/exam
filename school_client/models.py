#_*_encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class School(models.Model):
    name = models.CharField(max_length=128,verbose_name=u'学校名字')
    user = models.OneToOneField(User, verbose_name=u'注册用户')
    class Meta:
        verbose_name = '学校'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    GENDER_CHOICES = (
        (1, u'男'),
        (2, u'女'),
    )

    name = models.CharField(max_length=128,null=True,blank=True,verbose_name=u'教师姓名')
    school = models.ForeignKey(School,verbose_name=u'所在学校',null=True,blank=True)
    phone = models.CharField(max_length=128,verbose_name=u'电话', null=True, blank=True)
    province = models.CharField(max_length=128, verbose_name=u'籍贯', null=True, blank=True)
    location = models.TextField(verbose_name=u'地址', null=True, blank=True)
    idcard = models.CharField(max_length=128,verbose_name=u'身份证', null=True, blank=True)
    sex = models.IntegerField(choices=GENDER_CHOICES,null=True,blank=True)
    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name + '(' + self.school.name + ')'

class Exam(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True, verbose_name=u'考试名称')
    place = models.CharField(max_length=256,null=True,blank=True,verbose_name=u'考试地点')
    start = models.DateTimeField(null=True,blank=True,verbose_name=u'开始时间')
    end = models.DateTimeField(null=True, blank=True, verbose_name=u'结束时间')
    teacher = models.ManyToManyField(Teacher,verbose_name=u'监考老师')
    total = models.CharField(max_length=128, null=True, blank=True, verbose_name=u'总计')
    shui = models.CharField(max_length=128, null=True, blank=True, verbose_name=u'税收')

    class Meta:
        verbose_name = '考试'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name



