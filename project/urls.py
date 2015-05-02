from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('project.views',
    url( r'^$',              'projects'	   ),
    url( r'^project$',       'show_project'),
    url( r'^edit_project$',  'edit_project'),
    url( r'^edit_project/new$',  'edit_project', {'new' : True}),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)