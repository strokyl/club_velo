# -*- coding: utf-8 -*-
from django.contrib import admin
from club_velo.velo.models import *

class ReparationInline(admin.StackedInline):
    model = Reparation

class VeloAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_dentree'

    list_display = ('numero', 'date_dentree', 'marque', 'type', 'couleur')
    list_filter = ('numero', 'date_dentree', 'marque', 'type', 'couleur')

    search_fields = ['marque', 'type', 'couleur']

    fieldsets = (
            (None, {
                'fields' : ('numero', 'marque', 'type', 'couleur', 'date_dentree'),
                'description' : "Ces champs doivent être renseigné"
                }),
            ('Specificité techniques', {
                'fields' : ('tailleDeRoue', 'vitesse', 'plateau', 'suspension', 'sonette', 'bequille',
                    'frein_avant', 'frein_arriere', 'eclairage_avant', 'eclairage_arriere', 'porte_bagages_avant',
                    'porte_bagages_arriere')
                }),
            (None, {
                'fields' : ('remarque',)
                }),
            )

    inlines = [ReparationInline]

class MarqueAdmin(admin.ModelAdmin):
    list_display= ('marque',)

class TypeAdmin(admin.ModelAdmin):
    list_display= ('type',)

class TailleDeRoueAdmin(admin.ModelAdmin):
    list_display= ('taille',)

admin.site.register(Velo, VeloAdmin)
admin.site.register(Marque, MarqueAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(TailleDeRoue, TailleDeRoueAdmin)
