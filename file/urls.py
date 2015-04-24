from django.conf.urls import patterns, include, url

urlpatterns = patterns('file.views',
    url( r'^photos/upload$', 'upload', {'is_img': True}),
    url( r'^photos/recent$', 'recent', {'is_img': True}),
    url( r'^files/upload$', 'upload'),
    url( r'^files/recent$', 'recent'),
)
