from django.db import models


class Photo(models.Model):
    url = models.CharField(max_length=255)


class Ukulele(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)


class Guitar(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
