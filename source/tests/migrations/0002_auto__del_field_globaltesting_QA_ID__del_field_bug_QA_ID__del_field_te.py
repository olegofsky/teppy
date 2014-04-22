# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'GlobalTesting.QA_ID'
        db.delete_column('tests_globaltesting', 'QA_ID')

        # Deleting field 'Bug.QA_ID'
        db.delete_column('tests_bug', 'QA_ID')

        # Deleting field 'TestSuit.QA_ID'
        db.delete_column('tests_testsuit', 'QA_ID')

        # Deleting field 'TestCase.QA_ID'
        db.delete_column('tests_testcase', 'QA_ID')


    def backwards(self, orm):
        
        # Adding field 'GlobalTesting.QA_ID'
        db.add_column('tests_globaltesting', 'QA_ID', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Bug.QA_ID'
        db.add_column('tests_bug', 'QA_ID', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'TestSuit.QA_ID'
        db.add_column('tests_testsuit', 'QA_ID', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'TestCase.QA_ID'
        db.add_column('tests_testcase', 'QA_ID', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 14, 5, 22, 32, 43575)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 14, 5, 22, 32, 43464)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tests.bug': {
            'Meta': {'object_name': 'Bug'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bug_commiter'", 'to': "orm['auth.User']"}),
            'date_closed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_opened': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'gt': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tests.GlobalTesting']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'test_case': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tests.TestCase']"}),
            'traceback': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'tests.globaltesting': {
            'Meta': {'object_name': 'GlobalTesting'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'initiator'", 'to': "orm['auth.User']"}),
            'date_finish': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'test_cases': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tests.TestCase']", 'through': "orm['tests.TestCaseInGT']", 'symmetrical': 'False'}),
            'testers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'members'", 'symmetrical': 'False', 'to': "orm['auth.User']"})
        },
        'tests.testcase': {
            'Meta': {'object_name': 'TestCase'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cases_author'", 'to': "orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'developer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'expected_result': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'procedure': ('django.db.models.fields.TextField', [], {}),
            'producer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cases_spec_author'", 'to': "orm['auth.User']"}),
            'setup': ('django.db.models.fields.TextField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'suit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tests.TestSuit']", 'null': 'True', 'blank': 'True'})
        },
        'tests.testcaseingt': {
            'Meta': {'object_name': 'TestCaseInGT'},
            'gt': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tests.GlobalTesting']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'queued'", 'max_length': '16'}),
            'test_case': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tests.TestCase']"}),
            'tester': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'tests.testsuit': {
            'Meta': {'object_name': 'TestSuit'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'suits_author'", 'to': "orm['auth.User']"}),
            'global_setup': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'overview': ('django.db.models.fields.TextField', [], {}),
            'producer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'suits_spec_author'", 'to': "orm['auth.User']"}),
            'spec': ('django.db.models.fields.TextField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['tests']
