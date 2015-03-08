from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('forum.views',

    url( r'^(?P<id_project>\d+)$',            'forum'),
    url( r'^edit_forum/$',                    'edit_forum'),
    url( r'^edit_forum/(?P<id_project>\d+)$', 'edit_forum')
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)