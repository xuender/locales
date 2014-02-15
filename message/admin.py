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
    actions = ['exp_en', 'exp_zh_CN', 'exp_zh_TW', 'exp_ru']
    def exp(self, queryset, key):
        for i in queryset:
            f = open(i.path + '/' + key + '/messages.json', 'w')
            f.write('{\n')
            b = False
            for t in i.message_set.all():
                if b:
                    f.write(',\n')
                b = True
                f.write('   "' + t.code + '":{\n    "message": "')
                if key == 'en':
                    f.write(t.en)
                if key == 'zh_CN':
                    f.write(t.zh_CN.encode('utf-8'))
                if key == 'zh_TW':
                    f.write(t.zh_TW.encode('utf-8'))
                if key == 'ru':
                    f.write(t.ru.encode('utf-8'))
                f.write('"\n  }')
            f.write('\n}')
            f.close()

    def exp_en(self, request, queryset):
        self.exp(queryset, 'en')
        self.message_user(request, '英文被导出。')
    exp_en.short_description = '导出英文'
    def exp_zh_CN(self, request, queryset):
        self.exp(queryset, 'zh_CN')
        self.message_user(request, '简体中文被导出。')
    exp_zh_CN.short_description = '导出简体中文'
    def exp_zh_TW(self, request, queryset):
        self.exp(queryset, 'zh_TW')
        self.message_user(request, '繁体中文文件被导出。')
    exp_zh_TW.short_description = '导出繁体中文'
    def exp_ru(self, request, queryset):
        self.exp(queryset, 'ru')
        self.message_user(request, '俄文被导出。')
    exp_ru.short_description = '导出俄文'

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
