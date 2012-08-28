from django.contrib import admin
from apps.core.models import Entry, Category, Server

admin.site.register(Entry)
admin.site.register(Category)
admin.site.register(Server)