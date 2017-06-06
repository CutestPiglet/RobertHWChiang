import django
from django.shortcuts import render
from .models import AboutMe


def about(request):
    boxes = []

    # < about this site >
    contents = []
    contents.append({
        'p_text': 'Wrote by Django {}'.format(django.get_version()),
    })
    contents.append({
        'p_text': 'Host on',
        'a_text': 'Heroku',
        'a_href': 'https://www.heroku.com/'
    })
    contents.append({
        'p_text': 'Developed on Ubuntu 14.04'
    })
    contents.append({
        'p_text': 'Find source code on',
        'a_text': 'my GitHub repository',
        'a_href': 'https://github.com/RobertH-W-Chiang/RobertHWChiang'
    })
    boxes.append({
        'heading_img_url': 'img/about/site.jpg',
        'title': 'About This Site',
        'contents': contents
    })

    # < about me >
    contents = []
    for aboutme_obj in AboutMe.objects.all():
        contents.append({
            'p_text': aboutme_obj.text,
            'a_text': aboutme_obj.hyperlink_text,
            'a_href': aboutme_obj.hyperlink_url,
        })

    boxes.append({
        'heading_img_url': 'img/about/me.jpg',
        'title': 'About Me',
        'contents': contents
    })

    return render(request, 'about.html', {'boxes': boxes})
