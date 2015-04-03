from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout, login

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url (r'^project/(?P<id_project>\d+)', 'task_manager.views.show_project'), 
    
    url(r'^admin/',     include(admin.site.urls    )),    
    url(r'^',           include('auth.urls'        )),
    url(r'^auth/',      include('auth.urls'        )),
    url(r'^projects/',  include('project.urls'     )),
    url(r'^profile/',   include('user_profile.urls')),    
    url(r'^task/',      include('task.urls'        )),  
    url(r'^forum/',     include('forum.urls'       )), 
    url(r'^comment/',   include('comment.urls'     )),
    url(r'^statistic/', include('statistic.urls'   )),
    url(r'^iterates/',  include('iteration.urls'   )), 
    #url(r'^sign-out/$', logout, {'next_page':'/auth'},),
   # url(r'^sign-in/$', login, {'template_name': 'login.html', 'next_page': '/projects'},),
)
