# coding: utf-8
from django.test import Client
from django.test import TestCase
from project.models import Project
from iteration.models import Iteration
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import datetime, timedelta

import os.path

class ProjectTestCase(TestCase):

	def setUp(self):
		self.client = Client()
		user = self.client.post(reverse('register'), {'username': 'Mike', 'password1': '123', 'password2': '123'})
		us_id = User.objects.first().id
		self.test_data = {'title': 'Pro', 'text': 'some text', 'leader': us_id}

	def test_view_show_projects(self):
		response_create = self.client.get(reverse('projects'))
		self.assertEqual(response_create.status_code, 200)

	def test_view_create_show_project(self):
		response_form_new = self.client.get(reverse('edit_project'))
		self.assertEqual(response_form_new.status_code, 200)

		response_create = self.client.post(reverse('new_project'), self.test_data)
		self.assertEqual(response_create.status_code, 302)

		project_id = Project.objects.first().id

		response_edit = self.client.get(reverse('edit_project'), {'project_id': project_id})
		self.assertEqual(response_edit.status_code, 200)
		
		response_show = self.client.get(reverse('show_project'), {'project_id': project_id})
		self.assertEqual(response_show.status_code, 200)

