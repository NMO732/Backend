from django.test import TestCase
from rest_framework.test import APIClient
import unittest
from django.contrib.auth.models import User

# Create your tests here.

class TestUser1Api(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_user(self):
        url = 'http://127.0.0.1:8000/users/'
        response = self.client.get(url)
        #self.assertEqual(response.status_code,200)
        qs = User.objects.filter(first_name='Nikhil Kumar')
        self.assertEqual(qs.count(),3)
