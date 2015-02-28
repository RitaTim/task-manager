from django.contrib import admin
from django.contrib.auth.models import User

# def user_unicode(self):
#     return  u'%s, %s' % (self.last_name, self.first_name)

# User.__unicode__ = user_unicode

admin.site.unregister(User)
admin.site.register(User)