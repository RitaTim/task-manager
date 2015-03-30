from django.conf.urls import patterns, include, url

urlpatterns = patterns('user_profile.views',
    url(r'^$',                                   'profile'         ),
    url(r'^employees$',                          'employees'       ),
    url(r'get_tasks/(?P<iterate_id>\d+)$',       'get_tasks'       ),
    url(r'change_iterates/(?P<project_id>\d+)$', 'change_iterates' ),
    url(r'(?P<id_task>\d+)$',                    'get_task'        ),           
)