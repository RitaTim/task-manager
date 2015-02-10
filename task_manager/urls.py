from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout, login

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'task_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),    

    url(r'^auth/', include('auth.urls')),
    url(r'^projects/', include('project.urls')),
    url(r'^profile/', include('user_profile.urls')),
   # url(r'^sign-in/$', login, {'template_name': 'login.html', 'next_page': '/projects'},),
    url(r'^sign-out/$', logout, {'next_page':'/auth'},),
    url(r'^task/', include('task.urls')),

)
