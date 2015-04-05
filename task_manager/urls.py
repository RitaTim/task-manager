from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views       import logout, login
from django.contrib                  import admin
from django.conf.urls.static         import static
from django.conf.urls                import patterns, include, url
from django.conf                     import settings
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
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    )