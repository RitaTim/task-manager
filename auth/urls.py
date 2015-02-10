from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'task_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'auth.views.auth'),
    url(r'^login_user', 'django.contrib.auth.views.login', {'template_name': 'auth.html', 'redirect_field_name':'/projects'},), #'auth.views.login'),
    url(r'^logout_user', 'django.contrib.auth.views.logout', {'next_page':'/auth'},),

    url(r'^register', 'auth.views.register'),
    url(r'^register_success', 'auth.views.register_success'),
)