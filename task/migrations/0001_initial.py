# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Task'
        db.create_table(u'task_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('dead_line', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('iterate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['iteration.Iteration'], blank=True)),
            ('assigned', self.gf('django.db.models.fields.related.ForeignKey')(related_name='assigned', blank=True, to=orm['auth.User'])),
            ('entrasted', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entrasted', blank=True, to=orm['auth.User'])),
            ('main_task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['task.Task'], blank=True)),
            ('type_task', self.gf('django.db.models.fields.CharField')(default='task', max_length=1)),
            ('status', self.gf('django.db.models.fields.CharField')(default='not_dev', max_length=1)),
        ))
        db.send_create_signal(u'task', ['Task'])


    def backwards(self, orm):
        # Deleting model 'Task'
        db.delete_table(u'task_task')


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
            'assigned': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assigned'", 'blank': 'True', 'to': u"orm['auth.User']"}),
            'dead_line': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'entrasted': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entrasted'", 'blank': 'True', 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iterate': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['iteration.Iteration']", 'blank': 'True'}),
            'main_task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['task.Task']", 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'not_dev'", 'max_length': '1'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type_task': ('django.db.models.fields.CharField', [], {'default': "'task'", 'max_length': '1'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['task']