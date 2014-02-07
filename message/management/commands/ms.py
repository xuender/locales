#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# 上传已经messages.json
# Copyright © 2014 ender xu <xuender@gmail.com>
#
# Distributed under terms of the MIT license.

import logging
log = logging.getLogger('locales')
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
import os
import json
from path import path
from django.core.management.base import BaseCommand, CommandError
from message.models import App, Message

class Command(BaseCommand):
    '读取json文件'
    def handle(self, *args, **options):
        if len(args) < 3:
            log.info('help')
            log.info('./manager.py [应用代码] [语言代码] [messages.json文件]')
        else:
            app = App.objects.get(code=args[0])
            lang = args[1]
            data = json.loads(path(args[2]).text())
            for i in data:
                try:
                    m = Message.objects.get(code=i)
                    log.info(i)
                except:
                    m = Message(code=i)
                    m.zh_CN = ''
                    m.zh_TW = ''
                    m.ru = ''
                    m.en = ''
                if lang == 'en':
                    m.en = data[i]['message']
                if lang == 'zh_CN':
                    m.zh_CN = data[i]['message']
                if lang == 'zh_TW':
                    m.zh_TW = data[i]['message']
                if lang == 'ru':
                    m.ru = data[i]['message']
                m.save()
                m.apps.add(app)
                m.save()
