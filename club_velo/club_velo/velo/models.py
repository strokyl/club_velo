# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import Max
from club_velo import settings
import Image
import os


# Create your models here.

class Marque(models.Model):
    marque = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.marque

class Type(models.Model):
    type = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.type

class Couleur(models.Model):
    couleur = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.couleur

class Velo(models.Model):
    def delete(self, *args, **kwargs):
 

        for reparation in self.reparation_set.all():
            reparation.delete()

        super(Velo, self).delete(*args,**kwargs)




    def number():
        no = Velo.objects.all().aggregate(Max('numero'))
        if no == None or no['numero__max'] == None:
            return 1
        else:
            return no['numero__max'] + 1

    def __unicode__(self):
        return "Velo : %s %s %s" % (self.numero,self.marque, self.type)

    numero = models.PositiveIntegerField(unique=True, default=number)
    marque = models.ForeignKey(Marque)
    type = models.ForeignKey(Type)
    couleur = models.ForeignKey(Couleur)
    date_dentree =  models.DateField(verbose_name="Date d'entrée au club")

    photo = models.ImageField(upload_to='./',blank=True, null=True)

    tailleDeRoue = models.ForeignKey('TailleDeRoue', blank=True, null=True, verbose_name="taille de roue")
    vitesse = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1)])
    plateau = models.PositiveIntegerField(blank=True,  null=True, validators=[MinValueValidator(1)])
    suspension = models.BooleanField()
    sonette = models.BooleanField()
    bequille = models.BooleanField()
    frein_avant = models.ForeignKey('TypeDeFrein', blank=True, null=True, related_name="type_frein_avant")
    frein_arriere = models.ForeignKey('TypeDeFrein', blank=True, null=True, related_name="type_frein_arriere")
    eclairage_avant = models.BooleanField()
    eclairage_arriere = models.BooleanField()
    porte_bagages_avant = models.BooleanField()
    porte_bagages_arriere = models.BooleanField()

    remarque = models.TextField(blank=True)


    def save(self, *args, **kwargs):

        if self.id:
            previous = Velo.objects.get(id=self.id)  
            have_changed = self.photo and self.photo != previous.photo
        else:
            have_changed = True

        super(Velo, self).save(*args, **kwargs)
        
        if self.id is not None:  
            if have_changed:
                image = Image.open(self.photo.path)  
                image.thumbnail(settings.IMAGE_MAX_SIZE, Image.ANTIALIAS)  
                image.save(self.photo.path)  
                
    
class TailleDeRoue(models.Model):
    taille = models.PositiveIntegerField(unique=True)

    def __unicode__(self):
        return str(self.taille)

class Reparation(models.Model):
    date =  models.DateField()
    detail = models.TextField()
    velo = models.ForeignKey(Velo)

    def __unicode__(self):
        return "Reparation : %s %s"%(date, velo)

class TypeDeFrein(models.Model):
    typeDeFrein = models.CharField(verbose_name="type de frein", unique=True, max_length=64)

    def __unicode__(self):
        return self.typeDeFrein
