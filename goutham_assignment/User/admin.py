from django.contrib import admin
from .models import Post
from django.conf.locale.es import formats as es_formats

admin.site.register(Post)
es_formats.DATETIME_FORMAT = "d M Y"
