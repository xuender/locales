# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Message.code'
        db.alter_column(u'message_message', 'code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20))

    def backwards(self, orm):

        # Changing field 'Message.code'
        db.alter_column(u'message_message', 'code', self.gf('django.db.models.fields.CharField')(max_length=10, unique=True))

    models = {
        u'message.app': {
            'Meta': {'ordering': "['code']", 'object_name': 'App'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'message.message': {
            'Meta': {'ordering': "['code']", 'object_name': 'Message'},
            'apps': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['message.App']", 'symmetrical': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'en': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ru': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'zh_CN': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'zh_TW': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['message']