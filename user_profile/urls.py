from django.conf.urls import patterns, include, url

urlpatterns = patterns('user_profile.views',

    url(r'^$',                             'profile'   ),
    url(r'get_tasks/(?P<id_iterate>\d+)$', 'get_tasks' ),
    url(r'(?P<id_task>\d+)$',              'get_task'  ),        
)