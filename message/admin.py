# -*- coding: utf-8 -*-
from django.contrib import admin
from message.models import App, Message

def register(model):
    '''
    标注 django admin @register class decorator, e.g.
    @register(Entry)
    class EntryAdmin(models.ModelAdmin):
        pass
    '''
    def inner(admin_cls):
        admin.site.register(model, admin_cls)
        return admin_cls
    return inner

@register(App)
class AppAdmin(admin.ModelAdmin):
    '应用管理'
    search_fields = ['name', 'code', 'path', ]
    #date_hierarchy = 'create_at'
    #list_filter = ['hl', 'mode', 'type']
    list_display = ('name', 'code', )
    #readonly_fields = ('create_at', 'create_by', 'update_at', 'update_by', )
    fieldsets = [
        (
            None,
            {'fields': ['code', 'name', 'path', ]},
        ),
    ]

class AppInline(admin.TabularInline):
    model = Message.apps.through

@register(Message)
class MessageAdmin(admin.ModelAdmin):
    '信息管理'
    exclude = ('apps',)
    inlines = [AppInline,]
    search_fields = ['code', 'zh_CN', ]
    #date_hierarchy = 'create_at'
    list_filter = ['apps', ]
    list_display = ('code', 'zh_CN', 'en', )
    #readonly_fields = ('create_at', 'create_by', 'update_at', 'update_by', )
    fieldsets = [
        (
            None,
            {'fields': ['code', 'zh_CN', 'en', 'zh_TW', 'ru', ]},
        ),
    ]
