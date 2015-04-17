from django.test import TestCase
from project.models import Project
from django.contrib.auth.models import User
from django.test.client import Client

 
import os.path

class ProjectTestCase(TestCase):

	def setUp(self):
		test_user = User.objects.create(username='username')
		Project.objects.create(title="test_title", text="test_text", leader=test_user, id=1)

	def main_page(self):
		resp = self.client.get('/projects')
		self.assertIn(resp.status_code, [200, 301])

	def project_page(self):
		resp = self.client.get('/projects/project', { 'id': 1})
		self.assertIn(resp.status_code, [200, 301])
