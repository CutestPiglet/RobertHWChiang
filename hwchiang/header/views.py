import django
from django.shortcuts import render


def about(request):
    return render(request,
                  'about.html',
                  {'django_version': django.get_version()})


def resume(request):
    return render(request, 'resume.html')


def interests(request):
    return render(request, 'interests.html')
