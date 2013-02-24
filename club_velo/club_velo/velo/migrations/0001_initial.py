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
            ('marque', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
        ))
        db.send_create_signal('velo', ['Marque'])

        # Adding model 'Type'
        db.create_table('velo_type', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
        ))
        db.send_create_signal('velo', ['Type'])

        # Adding model 'Couleur'
        db.create_table('velo_couleur', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('couleur', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
        ))
        db.send_create_signal('velo', ['Couleur'])

        # Adding model 'Velo'
        db.create_table('velo_velo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, unique=True)),
            ('marque', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['velo.Marque'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['velo.Type'])),
            ('couleur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['velo.Couleur'])),
            ('date_dentree', self.gf('django.db.models.fields.DateField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('tailleDeRoue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['velo.TailleDeRoue'], null=True, blank=True)),
            ('vitesse', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('plateau', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('suspension', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sonette', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bequille', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('frein_avant', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='type_frein_avant', null=True, to=orm['velo.TypeDeFrein'])),
            ('frein_arriere', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='type_frein_arriere', null=True, to=orm['velo.TypeDeFrein'])),
            ('eclairage_avant', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('eclairage_arriere', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porte_bagages_avant', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porte_bagages_arriere', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('remarque', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('louer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_de_retour', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('mail_locataire', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('tel_locataire', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('prenom_locataire', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('nom_locataire', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
        ))
        db.send_create_signal('velo', ['Velo'])

        # Adding model 'TailleDeRoue'
        db.create_table('velo_taillederoue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('taille', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
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

        # Adding model 'TypeDeFrein'
        db.create_table('velo_typedefrein', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('typeDeFrein', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
        ))
        db.send_create_signal('velo', ['TypeDeFrein'])


    def backwards(self, orm):
        # Deleting model 'Marque'
        db.delete_table('velo_marque')

        # Deleting model 'Type'
        db.delete_table('velo_type')

        # Deleting model 'Couleur'
        db.delete_table('velo_couleur')

        # Deleting model 'Velo'
        db.delete_table('velo_velo')

        # Deleting model 'TailleDeRoue'
        db.delete_table('velo_taillederoue')

        # Deleting model 'Reparation'
        db.delete_table('velo_reparation')

        # Deleting model 'TypeDeFrein'
        db.delete_table('velo_typedefrein')


    models = {
        'velo.couleur': {
            'Meta': {'object_name': 'Couleur'},
            'couleur': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'velo.marque': {
            'Meta': {'object_name': 'Marque'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marque': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
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
            'taille': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        },
        'velo.type': {
            'Meta': {'object_name': 'Type'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        'velo.typedefrein': {
            'Meta': {'object_name': 'TypeDeFrein'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'typeDeFrein': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        'velo.velo': {
            'Meta': {'object_name': 'Velo'},
            'bequille': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'couleur': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['velo.Couleur']"}),
            'date_de_retour': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_dentree': ('django.db.models.fields.DateField', [], {}),
            'eclairage_arriere': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'eclairage_avant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'frein_arriere': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'type_frein_arriere'", 'null': 'True', 'to': "orm['velo.TypeDeFrein']"}),
            'frein_avant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'type_frein_avant'", 'null': 'True', 'to': "orm['velo.TypeDeFrein']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'louer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mail_locataire': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'marque': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['velo.Marque']"}),
            'nom_locataire': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'numero': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'unique': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'plateau': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'porte_bagages_arriere': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porte_bagages_avant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prenom_locataire': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'remarque': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sonette': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'suspension': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tailleDeRoue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['velo.TailleDeRoue']", 'null': 'True', 'blank': 'True'}),
            'tel_locataire': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['velo.Type']"}),
            'vitesse': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['velo']