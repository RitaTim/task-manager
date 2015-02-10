# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Task.main_task'
        db.alter_column(u'task_task', 'main_task_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['task.Task'], null=True))

        # Changing field 'Task.type_task'
        db.alter_column(u'task_task', 'type_task', self.gf('django.db.models.fields.CharField')(max_length=7))

        # Changing field 'Task.assigned'
        db.alter_column(u'task_task', 'assigned_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'Task.status'
        db.alter_column(u'task_task', 'status', self.gf('django.db.models.fields.CharField')(max_length=7))

        # Changing field 'Task.entrasted'
        db.alter_column(u'task_task', 'entrasted_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'Task.iterate'
        db.alter_column(u'task_task', 'iterate_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['iteration.Iteration'], null=True))

    def backwards(self, orm):

        # Changing field 'Task.main_task'
        db.alter_column(u'task_task', 'main_task_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['task.Task']))

        # Changing field 'Task.type_task'
        db.alter_column(u'task_task', 'type_task', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'Task.assigned'
        db.alter_column(u'task_task', 'assigned_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['auth.User']))

        # Changing field 'Task.status'
        db.alter_column(u'task_task', 'status', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'Task.entrasted'
        db.alter_column(u'task_task', 'entrasted_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['auth.User']))

        # Changing field 'Task.iterate'
        db.alter_column(u'task_task', 'iterate_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['iteration.Iteration']))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'iteration.iteration': {
            'Meta': {'object_name': 'Iteration'},
            'dead_line': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Project']"}),
            'start_line': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'project.project': {
            'Meta': {'object_name': 'Project'},
            'create_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leader': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'task.task': {
            'Meta': {'object_name': 'Task'},
            'assigned': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'assigned'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'dead_line': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'entrasted': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'entrasted'", 'null': 'True', 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iterate': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['iteration.Iteration']", 'null': 'True', 'blank': 'True'}),
            'main_task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['task.Task']", 'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'not_dev'", 'max_length': '7'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type_task': ('django.db.models.fields.CharField', [], {'default': "'task'", 'max_length': '7'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        }
    }

    complete_apps = ['task']