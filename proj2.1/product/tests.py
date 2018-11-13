from unittest.mock import patch, Mock
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from product.forms import RegisterForm
from product import views
from ddt import ddt, data, file_data, unpack

from product.models import Comment


class Testing(TestCase):
    def setUp(self):
        self.client = Client()

    """Method that return Comment instance"""
    def create_Comment_Object(self, comment="only a test"):
        return Comment.objects.create(comment=comment)

    """Model Testing"""

    def test_Comment_Model_creation(self):
        w = self.create_Comment_Object()
        self.assertTrue(isinstance(w, Comment))
        self.assertEqual('only a test', w.comment)

    def test_HV(self):
        x = views.Homeview()
        print(x)
        self.assertTrue(x)

    """Testing Request is Successful or not"""
    def test_registration(self):
        url = reverse_lazy('home')
        # test req method GET
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    """Testing Database based operation"""
    def test_get_user(self):
        user = User.objects.create(
            username='arbisoft',
            email='	m.usman@arbisoft.com',
            password = 'arbisoft'
        )
        self.assertEqual(User.objects.get(username='arbisoft'), user)

    """For Testing Json Response"""
    def test_jsonresponse(self):
        url = reverse_lazy('product:comment')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

        self.assertJSONEqual(response.content, {'comments': []})

    def test_verify_db(self):
        print(User.objects.all().count())
        self.assertEqual(User.objects.all().count(), 0)

    """Test For Template Verification"""
    def test_templateVerfication(self):
        url = reverse_lazy('home')
        # test req method GET
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'product/Home.html')

    @patch('product.views.Homeview.get_queryset')
    def test_HomeView(self, mock_get_queryset):
        url = reverse_lazy('home')
        self.assertEqual(mock_get_queryset.called, False)
        mock_get_queryset()
        self.assertEqual(mock_get_queryset.called, True)
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    @patch('product.views.Addproduct.success_url')
    def test_AddProduct(self, mock_success_url):
        mock_success_url = None
        self.assertEqual(mock_success_url,None)

    @patch('product.views.sendtofriend')
    def test_sends_mail_to_address_from_post(self, mock_send_mail):
        response = self.client.post('/product/send/5', data={
            'email': 'm.usman@arbisoft.com'
        })
        self.assertEqual(mock_send_mail.called, False)

    @patch('product.views.Homeview.get_queryset')
    def test_Home(self, get_queryset):
        url = reverse_lazy('home')
        self.assertEqual(get_queryset.called, False)

    """"Testing a form has valid Form data"""
    def test_UserForm_valid(self):
        form = RegisterForm(data={'username': "user", 'email': "user@mp.com", 'password': "user"})
        self.assertTrue(form.is_valid())

        # Testing a form has invalid Form data

    def test_UserForm_invalid(self):
        form = RegisterForm(data={'username': "", 'email': "user@mp.com", 'password': "user"})
        self.assertFalse(form.is_valid())

    """ Testing Html"""
    def test_home_page_contains_correct_html(self):
        url = reverse_lazy('home')
        response = self.client.get(url)
        self.assertContains(response, ' <title>Product Management System</title>')

    """test redirects"""
    def test_redirects_to_home_page(self):
        response = self.client.get('/product//' )
        self.assertRedirects(response, '/')

    """Adding Comment in Db With the help of Mock"""
    @patch('product.views.Comment1')
    def test_Add_Comment(self, mock_Comment1):
        mock = Mock()
        self.client.post('/product/comment/5', data={
            'comment': 'Mock Comment'
        })

    """Testing login View"""
    @patch('product.views.login')
    @patch('product.views.authenticate')
    def test_returns_OK_when_user_found(
            self, mock_authenticate, mock_login
    ):
        user = User.objects.create(username='a', password='a', email='a@gm.com')
        user.backend = ''  # required for auth_login to work
        mock_authenticate.return_value = user
        mock_login.return_value = 100
        re = mock_login()
        response = self.client.post('/product/login', data={
            'username': 'a',
            'password':'a'
        })
        self.assertEqual(response.status_code, 301)
        self.assertEqual(re, 100)


"""data drieven testing using dtt"""


@ddt
class FooTestCase(TestCase):
    def test_undecorated(self):
        self.assertTrue(2 < (24))

    @data(3, 4, 12, 23)
    def test_larger_than_two(self, value):
        self.assertTrue(2 < value)

    @data(1, -3, 2, 0)
    def test_not_larger_than_two(self, value):
        self.assertFalse(2 < value)

    @file_data("josonfile.json")
    def test_file_data_json_dict_dict(self, start, end, value):
        self.assertLess(start, end)
        self.assertLess(value, end)
        self.assertGreater(value, start)

    @data([3, 2], [4, 3], [5, 3])
    @unpack
    def test_list_extracted_into_arguments(self, first_value, second_value):
        self.assertTrue(first_value > second_value)

    @unpack
    @data({'first': 1, 'second': 3, 'third': 2},
          {'first': 4, 'second': 6, 'third': 5})
    def test_dicts_extracted_into_kwargs(self, first, second, third):
        self.assertTrue(first < third < second)

