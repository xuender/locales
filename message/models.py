# -*- coding: utf-8 -*-
from django.db import models

class App(models.Model):
    '应用'
    code = models.CharField(
            unique=True,
            max_length=10,
            help_text='最大10个字母',
            verbose_name='代码',
            )
    name = models.CharField(
            max_length=30,
            help_text='最大30个字母',
            verbose_name='名称',
            )
    path = models.CharField(
            max_length=200,
            help_text='最大200个字母',
            verbose_name='输出目录',
            )

    def __unicode__(self):
        return '%s(%s)'%(self.code, self.name)

    class Meta:
        verbose_name = '应用'
        verbose_name_plural = '应用'
        ordering = ['code',]

class Message(models.Model):
    '信息'
    apps = models.ManyToManyField(App)
    code = models.CharField(
            unique=True,
            max_length=20,
            help_text='最大10个字母',
            verbose_name='代码',
            )
    en = models.CharField(
            blank=True, null=True,
            max_length=500,
            help_text='最大500个字母',
            verbose_name='英文',
            )
    zh_CN = models.CharField(
            blank=True, null=True,
            max_length=500,
            help_text='最大500个字母',
            verbose_name='中文简体',
            )
    zh_TW = models.CharField(
            blank=True, null=True,
            max_length=500,
            help_text='最大500个字母',
            verbose_name='中文繁体',
            )
    ru = models.CharField(
            blank=True, null=True,
            max_length=500,
            help_text='最大500个字母',
            verbose_name='俄文',
            )
    def __unicode__(self):
        return '%s(%s)'%(self.code, self.zh_CN)
    class Meta:
        verbose_name = '信息'
        verbose_name_plural = '信息'
        ordering = ['code',]
