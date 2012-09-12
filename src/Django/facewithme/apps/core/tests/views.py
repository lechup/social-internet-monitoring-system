# -*- coding: utf-8 -*-
from django.test import Client, TestCase
from django.core.urlresolvers import reverse

from apps.core.tests.factories import StreamFactory, ServerFactory

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.server = ServerFactory.create()
        self.stream_list = StreamFactory.create_batch(15)


    def test_core_stream_list(self):
        response = self.client.get(reverse('core-stream_list'))
        
        # check if HTTP response code is 200
        self.assertEqual(response.status_code, 200)
        
        # check if view response contains title of first 5 items
        for i in range(0, len(self.stream_list)/2):
            self.assertContains(response, self.stream_list[i].title)
        

    def test_core_geoip_js(self):
        response = self.client.get(reverse('core-geoip_js'))