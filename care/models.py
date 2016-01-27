from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    image = models.FileField(null=True, blank=True)
    date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.text[:500]


class Certificate(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    image = models.FileField(null=True, blank=True)
    date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.text[:500]


class Brand(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    image = models.FileField(null=True, blank=True)
    date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.text[:500]


class Product(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    price = models.BigIntegerField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.text[:500]


class Contact(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    email = models.CharField(max_length=300)

    def __unicode__(self):
        return self.text[:500]


class Map(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    logo = models.FileField(null=True, blank=True)

    def __unicode__(self):
        return self.text[:500]


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    logo = models.FileField(null=True, blank=True)

    def __unicode__(self):
        return self.text[:500]
