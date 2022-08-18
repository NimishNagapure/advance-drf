from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login') 

        self.user_data = {
            'username': 'testuser',
            'email': 'email@email.com',
            'password':'email'
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
