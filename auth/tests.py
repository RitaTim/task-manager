# coding: utf-8
from django.test import Client
from django.test import TestCase
from django.core.urlresolvers import reverse

class AuthTest(TestCase):
	
	def setUp(self):
		"""initialize the Django test client"""
		self.client = Client()
		self.test_data = {'username': 'Mike', 'password1': '123', 'password2': '123'}

	def test_register(self):
		response = self.client.post(reverse('register'), self.test_data)
		self.assertEqual(response.status_code, 302)

	def test_logging(self):
		response = self.client.post(reverse('logging'), {'username': self.test_data['username'], 'password': self.test_data['password1']})
		self.assertEqual(response.status_code, 200)

	def test_logout(self):
		response = self.client.post(reverse('logout'))
		self.assertEqual(response.status_code, 302)

