# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Marque(models.Model):
    marque = models.CharField(max_length=64)

    def __unicode__(self):
        return self.marque

class Type(models.Model):
    type = models.CharField(max_length=64)

    def __unicode__(self):
        return self.type

class Velo(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    marque = models.ForeignKey(Marque)
    type = models.ForeignKey(Type)
    couleur = models.CharField(max_length=64)
    date_dentree =  models.DateField(verbose_name="Date d'entrée au club")

    tailleDeRoue = models.ForeignKey('TailleDeRoue', blank=True, null=True, verbose_name="taille de roue")
    vitesse = models.PositiveIntegerField(blank=True, validators=[MinValueValidator(1)])
    plateau = models.PositiveIntegerField(blank=True,  validators=[MinValueValidator(1)])
    suspension = models.BooleanField()
    sonette = models.BooleanField()
    bequille = models.BooleanField()
    frein_avant = models.BooleanField()
    frein_arriere = models.BooleanField()
    eclairage_avant = models.BooleanField()
    eclairage_arriere = models.BooleanField()
    porte_bagages_avant = models.BooleanField()
    porte_bagages_arriere = models.BooleanField()

    remarque = models.TextField(blank=True)
    
class TailleDeRoue(models.Model):
    taille = models.PositiveIntegerField()

    def __unicode__(self):
        return str(self.taille)

class Reparation(models.Model):
    date =  models.DateField()
    detail = models.TextField()
    velo = models.ForeignKey(Velo)

