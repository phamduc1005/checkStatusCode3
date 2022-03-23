from django.db import models
from datetime import datetime


class CheckUrl(models.Model):
    test = models.CharField(max_length=20)
    time = models.DateTimeField(default=datetime.now) 

class UrlError(models.Model):
    checkUrl = models.ForeignKey(CheckUrl, related_name='error', on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField()
    url = models.CharField(max_length=200)