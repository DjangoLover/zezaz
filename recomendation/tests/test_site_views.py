# -*- coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse


class SiteViewsTest(TestCase):

    def test_home_view(self):
        response = self.client.get(reverse('recomendation:home'))

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'home.html')

    def test_about_view(self):
        response = self.client.get(reverse('recomendation:about'))

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'about.html')

    def test_team_view(self):
        response = self.client.get(reverse('recomendation:team'))

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'team.html')

