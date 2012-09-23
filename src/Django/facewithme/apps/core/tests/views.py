# -*- coding: utf-8 -*-
from django.test import Client, TestCase
from django.core.urlresolvers import reverse

from apps.core.tests.factories import StreamFactory, ServerFactory

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.server = ServerFactory.create()
        self.stream_list = StreamFactory.create_batch(10)

    def test_core_stream_list(self):
        response = self.client.get(reverse('core-stream_list'))

        # check if HTTP response code is 200
        self.assertEqual(response.status_code, 200)

        # check if view response contains title of first 5 items
        for i in self.stream_list[-3:]:
            self.assertContains(response, i.title)

    def test_core_about(self):
        response = self.client.get(reverse('core-about'))
        # check if HTTP response code is 200
        self.assertEqual(response.status_code, 200)

    def test_core_help(self):
        response = self.client.get(reverse('core-help'))
        # check if HTTP response code is 200
        self.assertEqual(response.status_code, 200)

    def test_core_geoip_js(self):
        response = self.client.get(reverse('core-geoip_js'))
        # check if HTTP response code is 200
        self.assertEqual(response.status_code, 200)

    def test_core_crossdomain_xml(self):
        response = self.client.get(reverse('core-crossdomain_xml'))
        # check if HTTP response code is 200
        self.assertEqual(response.status_code, 200)

    def test_core_robots_txt(self):
        response = self.client.get(reverse('core-robots_txt'))
        # check if HTTP response code is 200
        self.assertEqual(response.status_code, 200)
