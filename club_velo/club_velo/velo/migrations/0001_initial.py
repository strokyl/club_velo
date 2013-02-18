# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Marque'
        db.create_table('velo_marque', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marque', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('velo', ['Marque'])

        # Adding model 'Type'
        db.create_table('velo_type', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('velo', ['Type'])

        # Adding model 'Velo'
        db.create_table('velo_velo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
            ('marque', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['velo.Marque'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['velo.Type'])),
            ('couleur', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('date_dentree', self.gf('django.db.models.fields.DateField')()),
            ('tailleDeRoue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['velo.TailleDeRoue'], blank=True)),
            ('vitesse', self.gf('django.db.models.fields.PositiveIntegerField')(blank=True)),
            ('plateau', self.gf('django.db.models.fields.PositiveIntegerField')(blank=True)),
            ('suspension', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sonette', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bequille', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('frein_avant', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('frein_arriere', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('eclairage_avant', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('eclairage_arriere', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porte_bagages_avant', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porte_bagages_arriere', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('remarque', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('velo', ['Velo'])

        # Adding model 'TailleDeRoue'
        db.create_table('velo_taillederoue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('taille', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('velo', ['TailleDeRoue'])

        # Adding model 'Reparation'
        db.create_table('velo_reparation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('detail', self.gf('django.db.models.fields.TextField')()),
            ('velo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['velo.Velo'])),
        ))
        db.send_create_signal('velo', ['Reparation'])


    def backwards(self, orm):
        # Deleting model 'Marque'
        db.delete_table('velo_marque')

        # Deleting model 'Type'
        db.delete_table('velo_type')

        # Deleting model 'Velo'
        db.delete_table('velo_velo')

        # Deleting model 'TailleDeRoue'
        db.delete_table('velo_taillederoue')

        # Deleting model 'Reparation'
        db.delete_table('velo_reparation')


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
            'tailleDeRoue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['velo.TailleDeRoue']", 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['velo.Type']"}),
            'vitesse': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['velo']