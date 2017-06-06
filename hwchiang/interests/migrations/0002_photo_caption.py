# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='caption',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
