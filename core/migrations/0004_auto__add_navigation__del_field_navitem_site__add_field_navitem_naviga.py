# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Navigation'
        db.create_table('core_navigation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('core', ['Navigation'])

        # Deleting field 'NavItem.site'
        db.delete_column('core_navitem', 'site')

        # Adding field 'NavItem.navigation'
        db.add_column('core_navitem', 'navigation', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['core.Navigation']), keep_default=False)

        # Adding field 'NavItem.label'
        db.add_column('core_navitem', 'label', self.gf('django.db.models.fields.CharField')(default=1, max_length=100), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Navigation'
        db.delete_table('core_navigation')

        # Adding field 'NavItem.site'
        db.add_column('core_navitem', 'site', self.gf('django.db.models.fields.CharField')(default=1, max_length=100), keep_default=False)

        # Deleting field 'NavItem.navigation'
        db.delete_column('core_navitem', 'navigation_id')

        # Deleting field 'NavItem.label'
        db.delete_column('core_navitem', 'label')


    models = {
        'core.navigation': {
            'Meta': {'object_name': 'Navigation'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.navitem': {
            'Meta': {'object_name': 'NavItem'},
            'display_order': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'navigation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Navigation']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.settings': {
            'Meta': {'object_name': 'Settings'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_overview': ('django.db.models.fields.TextField', [], {}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'tagline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'BioMart'", 'max_length': '100'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['core']
