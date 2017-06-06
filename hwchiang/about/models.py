from django.db import models


class AboutMe(models.Model):
    text = models.CharField(max_length=50)
    hyperlink_text = models.CharField(max_length=50)
    hyperlink_url = models.CharField(max_length=255)
