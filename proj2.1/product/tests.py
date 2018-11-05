from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse



def setUp(self):
    self.client = Client()


def test_registration(self):
    url = reverse('signup')

    # test req method GET
    response = self.client.get(url)
    self.assertEqual(response.status, 200)


def test_blank_data(self):
    url = reverse('signup')
    response = self.client.post(url, {})
    self.assertEqual(response.status, 200)
    exp_data = {
        'error': True,
        'errors': {
            'username': 'This field is required',
            'email': 'This field is required',
            'password': 'This field is required',
        }
    }
    self.asssertEqual(exp_data, response.json())


def test_get_authors(self):
    user = User.objects.create(
        username='arbisoft',
        email='	m.usman@arbisoft.com'
    )
    self.assertEqual(User.objects.filter(id=0), user)
