# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Velo.photo_miniature'
        db.add_column('velo_velo', 'photo_miniature',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Velo.tel_locataire'
        db.alter_column('velo_velo', 'tel_locataire', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

    def backwards(self, orm):
        # Deleting field 'Velo.photo_miniature'
        db.delete_column('velo_velo', 'photo_miniature')


        # User chose to not deal with backwards NULL issues for 'Velo.tel_locataire'
        raise RuntimeError("Cannot reverse this migration. 'Velo.tel_locataire' and its values cannot be restored.")

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
            'numero': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2', 'unique': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo_miniature': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'plateau': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'porte_bagages_arriere': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porte_bagages_avant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prenom_locataire': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'remarque': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sonette': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'suspension': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tailleDeRoue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['velo.TailleDeRoue']", 'null': 'True', 'blank': 'True'}),
            'tel_locataire': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['velo.Type']"}),
            'vitesse': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['velo']