# -*- coding: utf-8 -*-
from django.contrib import admin
from club_velo.velo.models import *

class ReparationInline(admin.StackedInline):
    model = Reparation
    extra = 1

class VeloAdmin(admin.ModelAdmin):
    model = Velo
    date_hierarchy = 'date_dentree'

    list_display = ('numero', 'date_dentree', 'marque', 'type', 'couleur')
    list_filter = ('date_dentree', 'marque', 'type', 'couleur', 'frein_avant', 'frein_arriere', 'suspension', 'bequille','porte_bagages_avant', 'porte_bagages_arriere', 'sonette')

    #radio_fields = {"type" : admin.HORIZONTAL, "marque" : admin.HORIZONTAL, "tailleDeRoue" : admin.HORIZONTAL}

    search_fields = ['marque', 'type', 'couleur']

    fieldsets = (
            (None, {
                'fields' : ('numero', 'marque', 'type', 'couleur', 'date_dentree', 'photo'),
                'description' : "Ces champs doivent être renseigné"
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
