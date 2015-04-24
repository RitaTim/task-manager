# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'File'
        db.create_table(u'file_file', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('upload', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_image', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'file', ['File'])


    def backwards(self, orm):
        # Deleting model 'File'
        db.delete_table(u'file_file')


    models = {
        u'file.file': {
            'Meta': {'object_name': 'File'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_image': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'upload': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['file']