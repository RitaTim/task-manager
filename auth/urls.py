from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout

urlpatterns = patterns('',
    url(r'^login_user',  'django.contrib.auth.views.login', {'template_name': 'auth.html', 'redirect_field_name':'/projects'},),
    url(r'^logout_user', 'django.contrib.auth.views.logout', {'next_page':'/auth'},),

    url(r'^$',                'auth.views.auth_form'),
    url(r'^register',         'auth.views.register'),
    url(r'^register_success', 'auth.views.register_success'),
)