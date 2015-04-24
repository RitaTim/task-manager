from django.conf.urls import patterns, include, url

urlpatterns = patterns('notification.views',

    url( r'^get_notification$', 'get_notification'),
)