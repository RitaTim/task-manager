import datetime

from django.db import models

def get_uploaded_file_name(instance, filename):
	return "redactor/%s" % filename

class File(models.Model):
	upload = models.FileField(upload_to=get_uploaded_file_name)
	created = models.DateTimeField(default=datetime.datetime.now)
	is_image = models.BooleanField(default=True)