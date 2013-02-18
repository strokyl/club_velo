# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Velo.tailleDeRoue'
        db.alter_column('velo_velo', 'tailleDeRoue_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['velo.TailleDeRoue'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Velo.tailleDeRoue'
        raise RuntimeError("Cannot reverse this migration. 'Velo.tailleDeRoue' and its values cannot be restored.")

    models = {
        'velo.marque': {
            'Meta': {'object_name': 'Marque'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marque': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'velo.reparation': {
            'Meta': {'object_name': 'Reparation'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'detail': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'velo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['velo.Velo']"})
        },
        'velo.taillederoue': {
            'Meta': {'object_name': 'TailleDeRoue'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'taille': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'velo.type': {
            'Meta': {'object_name': 'Type'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'velo.velo': {
            'Meta': {'object_name': 'Velo'},
            'bequille': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'couleur': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'date_dentree': ('django.db.models.fields.DateField', [], {}),
            'eclairage_arriere': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'eclairage_avant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'frein_arriere': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'frein_avant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marque': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['velo.Marque']"}),
            'numero': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'plateau': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'porte_bagages_arriere': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porte_bagages_avant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'remarque': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sonette': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'suspension': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tailleDeRoue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['velo.TailleDeRoue']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['velo.Type']"}),
            'vitesse': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['velo']