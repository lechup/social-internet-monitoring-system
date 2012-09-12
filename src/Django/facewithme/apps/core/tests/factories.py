# -*- coding: utf-8 -*-
import factory
import random

from django.contrib.auth.models import User

from apps.core.models import Stream, Category, Server

class ServerFactory(factory.Factory):
    FACTORY_FOR = Server
    name = factory.Sequence(lambda n: "This is test OpenRTMFP server number" + n)
    url = 'rtmfp://108.59.252.39/2ad53ba05ab0437da544-8adb73046434'


class StreamFactory(factory.Factory):
    FACTORY_FOR = Stream
    title = factory.Sequence(lambda n: "This is test stream number" + n)
    
    @factory.post_generation(extract_prefix='categories')
    def add_categories(self, create, extracted, **kwargs):
        for category in Category.objects.all().order_by('?')[:random.randint(1, 3)]:
            self.categories.add(category)


class UserFactory(factory.Factory):
    FACTORY_FOR = User

    first_name = u'Leszek'
    last_name = u'Piątek'
    admin = False

    @factory.post_generation
    def password(self, user):
        user.set_password('foo')
        user.save()


class StreamWithUserFactory(StreamFactory):
    user = factory.SubFactory(UserFactory)
