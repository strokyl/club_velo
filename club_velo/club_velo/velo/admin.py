# -*- coding: utf-8 -*-
from django.contrib import admin
from club_velo.velo.models import *
from django.contrib.localflavor.fr.forms import FRPhoneNumberField
from django.forms import ModelForm

class ReparationInline(admin.StackedInline):
    model = Reparation
    extra = 1

class VeloForm(ModelForm):
    tel_locataire = FRPhoneNumberField()

    class Meta:
        model = Velo

class VeloAdmin(admin.ModelAdmin):
    model = Velo
    date_hierarchy = 'date_dentree'

    list_display = ('numero','admin_thumbnail', 'date_dentree', 'marque', 'type', 'couleur', 'mail_locataire')
    list_filter = ('louable', 'date_dentree', 'marque', 'type', 'couleur', 'frein_avant', 'frein_arriere', 'suspension', 'bequille','porte_bagages_avant', 'porte_bagages_arriere', 'sonette', 'louer')

    #radio_fields = {"type" : admin.HORIZONTAL, "marque" : admin.HORIZONTAL, "tailleDeRoue" : admin.HORIZONTAL}

    search_fields = ['numero','marque__marque', 'type__type', 'couleur__couleur', 'mail_locataire','nom_locataire','prenom_locataire', 'date_dentree', 'date_de_retour','remarque','prenom_locataire','nom_locataire']

    fieldsets = (
            (None, {
                'fields' : ('numero', 'marque', 'type', 'couleur', 'date_dentree', 'photo'),
                'description' : "Ces champs doivent être renseigné"
                }),
            ('Location', {
                'fields' : ('louable', 'louer', 'date_de_retour','mail_locataire','tel_locataire','prenom_locataire','nom_locataire'),
                }),
            ('Specificité techniques', {
                'fields' : ('tailleDeRoue', 'vitesse', 'plateau', 'suspension', 'sonette', 'bequille'),
                }),
            ('Frein', {
                'fields' : ('frein_avant', 'frein_arriere')
                }),
            ('Eclairage', {
                'fields' : ('eclairage_avant', 'eclairage_arriere')
                }),
            ('Porte Bagages', {
                'fields' : ('porte_bagages_avant', 'porte_bagages_arriere')
                }),
            ('Remarque', {
                'fields' : ('remarque',)
                }),
            )

    inlines = [ReparationInline]

class MarqueAdmin(admin.ModelAdmin):
    model = Marque
    list_display= ('marque',)

class TypeAdmin(admin.ModelAdmin):
    model = Type
    list_display= ('type',)

class CouleurAdmin(admin.ModelAdmin):
    model = Couleur
    list_display= ('couleur',)

class TypeDeFreinAdmin(admin.ModelAdmin):
    model = Type
    list_display= ('typeDeFrein',)

class TailleDeRoueAdmin(admin.ModelAdmin):
    model = TailleDeRoue
    list_display= ('taille',)

admin.site.register(TypeDeFrein, TypeDeFreinAdmin)
admin.site.register(Velo, VeloAdmin)
admin.site.register(Couleur, CouleurAdmin)
admin.site.register(Marque, MarqueAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(TailleDeRoue, TailleDeRoueAdmin)
