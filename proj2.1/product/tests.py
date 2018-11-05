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


def test_blank_data(self):
    form = RegisterForm({}, entry=self.entry)
    self.assertFalse(form.is_valid())
    self.assertEqual(form.errors, {
        'username': ['required'],
        'email': ['required'],
        'password': ['required'],
    })


def test_get_authors(self):
    user = User.objects.create(
        username='arbisoft',
        email='	m.usman@arbisoft.com'
    )
    self.assertEqual(User.objects.filter(id=0), user)
