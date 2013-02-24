# -*- coding: utf-8 -*-
from django.core.files.uploadedfile import SimpleUploadedFile
from StringIO import StringIO
from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import Max
from club_velo import settings

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

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

    def admin_thumbnail(self):
        if self.photo_miniature.url:
            return u'<a href="%s"><img src="%s" /></a>' % (self.photo.url, self.photo_miniature.url)
        else:
            return ""

    admin_thumbnail.short_description = 'Photo'
    admin_thumbnail.allow_tags = True

    def __unicode__(self):
        return "Velo : %s %s %s" % (self.numero,self.marque, self.type)

    numero = models.PositiveIntegerField(unique=True, default=number)
    marque = models.ForeignKey(Marque)
    type = models.ForeignKey(Type)
    couleur = models.ForeignKey(Couleur)
    date_dentree =  models.DateField(verbose_name="Date d'entrée au club")

    photo = ProcessedImageField(upload_to='velo', blank=True, null=True,
            processors=[ResizeToFill(1024,768)],
            format='JPEG',
            options={'quality':70})

    photo_miniature = ImageSpecField(image_field='photo',
            processors=[ResizeToFill(150,150)],
            options={'quality':70})

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

    louer = models.BooleanField(verbose_name="loué")
    louable = models.BooleanField()
    date_de_retour = models.DateField(blank=True, null=True)
    mail_locataire = models.EmailField(blank=True, null=True)
    tel_locataire = models.CharField(max_length=32, blank=True, null=True)
    prenom_locataire = models.CharField(max_length=64, blank=True, null=True)
    nom_locataire = models.CharField(max_length=64, blank=True, null=True)
                
    
class TailleDeRoue(models.Model):
    taille = models.PositiveIntegerField(unique=True)

    def __unicode__(self):
        return str(self.taille)

class Reparation(models.Model):
    date =  models.DateField()
    detail = models.TextField()
    velo = models.ForeignKey(Velo)

    def __unicode__(self):
        return "Reparation : %s %s"%(self.date, self.velo)

class TypeDeFrein(models.Model):
    typeDeFrein = models.CharField(verbose_name="type de frein", unique=True, max_length=64)

    def __unicode__(self):
        return self.typeDeFrein
