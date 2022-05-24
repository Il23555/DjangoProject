from django.test import TestCase, Client


# Create your tests here.

class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_loads_movies(self):
        response = self.client.get('app/movie')
        self.assertEqual(response.status_code, 200)

    def test_login_user(self):
        credentials = {
            'username': 'user122',
            'password': 'qqqqqqqq'
        }
        response = self.client.post('/signup', credentials, follow=True)
        self.assertEqual(response.status_code, 200)
