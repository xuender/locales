# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'App'
        db.create_table(u'message_app', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'message', ['App'])

        # Adding model 'Message'
        db.create_table(u'message_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('en', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('zh_CN', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('zh_TW', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('ru', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal(u'message', ['Message'])

        # Adding M2M table for field apps on 'Message'
        m2m_table_name = db.shorten_name(u'message_message_apps')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('message', models.ForeignKey(orm[u'message.message'], null=False)),
            ('app', models.ForeignKey(orm[u'message.app'], null=False))
        ))
        db.create_unique(m2m_table_name, ['message_id', 'app_id'])


    def backwards(self, orm):
        # Deleting model 'App'
        db.delete_table(u'message_app')

        # Deleting model 'Message'
        db.delete_table(u'message_message')

        # Removing M2M table for field apps on 'Message'
        db.delete_table(db.shorten_name(u'message_message_apps'))


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
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'en': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ru': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'zh_CN': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'zh_TW': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['message']