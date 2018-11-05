from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse_lazy

def setUp(self):
    self.client = Client()


def test_registration(self):
    url = reverse_lazy('signup')

    # test req method GET
    response = self.client.get(url)
    self.assertEqual(response.status, 200)
