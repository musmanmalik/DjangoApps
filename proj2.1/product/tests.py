from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_text


class Testing(TestCase):

    def setUp(self):
        self.client = Client()

    def test_registration(self):
        url = reverse_lazy('home')
        print(url)
        # test req method GET
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # #to test weather the required feilds are missing or not
    # def test_blank_data(self):
    #     url = reverse_lazy('product:signup')
    #     response = self.client.post(url, {})
    #     self.assertEqual(response.status_code, 200)
    #     exp_data = {
    #         'error': True,
    #         'errors': {
    #             'username': 'This field is required',
    #             'email': 'This field is required',
    #             'password': 'This field is required',
    #         }
    #     }
    #     self.assertEqual(exp_data, response.content)

    def test_get_authors(self):
        user = User.objects.create(
            username='arbisoft',
            email='	m.usman@arbisoft.com',
            password = 'arbisoft'
        )
        self.assertEqual(User.objects.get(username='arbisoft'), user)

    def test_jsonresponse(self):
        url = reverse_lazy('product:comment')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

        self.assertJSONEqual(response.content, {'comments': []})
