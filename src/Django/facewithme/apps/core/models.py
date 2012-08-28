# -*- coding: utf-8 -*-
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as gis_models

from lib.slughifi import slughifi


def get_uuid():
    return str(uuid.uuid4())
def get_server():
    try:
        # get random server
        server = Server.objects.all().order_by('?')[0]
    except:
        server = None
    return server

class Entry(models.Model):
    uuid = models.CharField(
        max_length = 36,
        primary_key = True,
        default = get_uuid,
        editable = False
    )
    title = models.CharField(
        u'tytuł',
        max_length = 255,
    )
    slug = models.SlugField(
        u'slug tytułu',
        max_length = 255,
        editable = False,
        unique = True
    )
    start = models.DateTimeField(
        auto_now_add = True,
        editable = False
    )
    user = models.ForeignKey(
         User,
         null = True,
         blank = True,
         default = None
    )
    server = models.ForeignKey(
       'Server',
       default=get_server
    )
    categories = models.ManyToManyField('Category')
    is_public = models.BooleanField(default = True)
    # GIS
    coordinates = gis_models.PointField(null = True, blank = True)
    objects = gis_models.GeoManager()

    @models.permalink
    def get_absolute_url(self):
        if self.is_public:
            return ('core:receivingview', (), {
                    'slug': self.slug
                }
            )
        else:
            return ('core:receivingprivateview', (), {
                    'uuid': self.uuid,
                    'slug': self.slug
                }
            )


    def save(self, *args, **kwargs):
        self.slug = slughifi(self.title)
        return super(Entry, self).save(*args, **kwargs)


    def __unicode__(self):
        return u'%s' % (self.slug)


class Category(models.Model):
    name = models.CharField(u'nazwa', max_length=100)
    value = models.CharField(u'wartość', max_length=100, default="")
    
    def __unicode__(self):
        return u'%s' % (self.name)


class Server(models.Model):
    name = models.CharField(u'nazwa', max_length=100)
    url = models.CharField(u'url', max_length=255)
    
    def __unicode__(self):
        return u'%s' % (self.name)