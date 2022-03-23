from django.contrib import admin
from .models import CheckUrl, UrlError
# Register your models here.
admin.site.register(CheckUrl)
admin.site.register(UrlError)
