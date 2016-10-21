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
        'p_text': 'Flickr:',
        'a_text': 'https://www.flickr.com/photos/johnmay0629',
        'a_href': 'https://www.flickr.com/photos/johnmay0629'
    })
    contents.append({
        'p_text': 'Youtube:',
        'a_text': 'https://www.youtube.com/user/johnmay0629',
        'a_href': 'https://www.youtube.com/user/johnmay0629/videos'
    })
    contents.append({
        'p_text': 'Facebook:',
        'a_text': 'https://www.facebook.com/johnmay0629',
        'a_href': 'https://www.facebook.com/johnmay0629'
    })
    boxes.append({
        'heading_img_url': 'img/about/me.jpg',
        'title': 'About Me',
        'contents': contents
    })
    return render(request, 'about.html', {'boxes': boxes})


def resume(request):
    return render(request, 'resume.html')


def interests(request):
    photos = [
        'https://c4.staticflickr.com/8/7457/27001286083_555761a5b2_k.jpg',
        'https://c7.staticflickr.com/8/7548/27511001622_e282be32cf_k.jpg',
        'https://c3.staticflickr.com/8/7651/27000443114_27fd6a0d5d_k.jpg',
        'https://c3.staticflickr.com/8/7392/27576694866_7e21f2c2c1_k.jpg',
        'https://c7.staticflickr.com/8/7057/27576783726_af06057eda_k.jpg',
        'https://c8.staticflickr.com/8/7710/27001449223_bc34f254f0_k.jpg',
        'https://c6.staticflickr.com/2/1608/25642761653_d93c7b3626_k.jpg',
        'https://c2.staticflickr.com/6/5708/23053158129_773fd151f2_k.jpg',
        'https://c5.staticflickr.com/1/769/23113079740_3181322f1f_k.jpg',
        'https://c7.staticflickr.com/1/640/21730761646_9a0b88e1f7_k.jpg',
        'https://c3.staticflickr.com/1/687/21134156074_a74ece7a8d_k.jpg',
        'https://c8.staticflickr.com/6/5743/21570012639_0742ee75f4_k.jpg',
        'https://c3.staticflickr.com/1/738/21568861250_cc275cb73a_k.jpg',
        'https://c8.staticflickr.com/6/5633/21756843815_da7943e992_k.jpg',
        'https://c2.staticflickr.com/1/484/19040851945_0205256354_k.jpg',
        'https://c4.staticflickr.com/8/7681/17275119851_bf120f3343_k.jpg',
        'https://c4.staticflickr.com/8/7700/17112375307_10317f34da_k.jpg',
        'https://c2.staticflickr.com/9/8642/16619700665_e867da6090_k.jpg',
        'https://c8.staticflickr.com/9/8618/16026663127_5203149889_k.jpg',
        'https://c5.staticflickr.com/8/7575/16025132820_7a254a0a4f_k.jpg',
        'https://c7.staticflickr.com/8/7569/15590078734_8d3db1c2db_k.jpg']
    return render(request, 'interests.html', {'photos': photos})
