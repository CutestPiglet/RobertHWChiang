import django
from django.shortcuts import render


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
    contents.append({
        'p_text': 'Email:',
        'a_text': 'johnmay0629@gmail.com',
        'a_href': 'mailto:johnmay0629@gmail.com'
    })
    contents.append({
        'p_text': 'Blogger:',
        'a_text': 'http://roberthwchiang.blogspot.tw',
        'a_href': 'http://roberthwchiang.blogspot.tw'
    })
    contents.append({
        'p_text': 'Flickr:',
        'a_text': 'https://www.flickr.com/photos/johnmay0629',
        'a_href': 'https://www.flickr.com/photos/johnmay0629'
    })
    contents.append({
        'p_text': 'Youtube:',
        'a_text': 'https://www.youtube.com/user/johnmay0629',
        'a_href': 'https://www.youtube.com/user/johnmay0629/videos'
    })
    boxes.append({
        'heading_img_url': 'img/about/me.jpg',
        'title': 'About Me',
        'contents': contents
    })

    return render(request, 'about.html', {'boxes': boxes})
