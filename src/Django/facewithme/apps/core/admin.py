from django.contrib import admin
from apps.core.models import Stream, Category, Server

admin.site.register(Stream)
admin.site.register(Category)
admin.site.register(Server)