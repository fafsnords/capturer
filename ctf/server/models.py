from django.db import models

class Cipher(models.Model):
   cipher = models.CharField(max_length=404)

class Stegano(models.Model):
   stegano = models.CharField(max_length=404)

class ReverseEngr(models.Model):
   reverseengr = models.CharField(max_length=404)

class Analysis(models.Model):
   analysis = models.CharField(max_length=404)

class DirListing(models.Model):
   dirlisting = models.CharField(max_length=404)

class Recon(models.Model):
   recon = models.CharField(max_length=404)