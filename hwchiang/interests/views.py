# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Photo, Ukulele, Guitar


def interests(request):
    # < photography >
    photos = []
    for photo_obj in Photo.objects.all():
        photos.append({
            'url': photo_obj.url,
            'caption': photo_obj.caption,
        })

    # < ukulele >
    ukuleles = []
    for ukulele_obj in Ukulele.objects.all():
        ukuleles.append({
            'title': ukulele_obj.title,
            'video_url': ukulele_obj.url,
        })

    # < guitar >
    guitars = []
    for guitar_obj in Guitar.objects.all():
        guitars.append({
            'title': guitar_obj.title,
            'video_url': guitar_obj.url,
        })

    return render(request,
                  'interests.html',
                  {'photos': photos,
                   'ukuleles': ukuleles,
                   'guitars': guitars})
