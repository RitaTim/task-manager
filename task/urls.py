from django.conf.urls import patterns, include, url

urlpatterns = patterns('task.views',

    url( r'^tasks/(?P<id_project>\d+)$',             'show_tasks'    ),
    url( r'^dashboard/(?P<id_project>\d+)$',         'show_dashboard'),
    url( r'^task$',            				         'task'          ),
    url( r'^task/(?P<id_task>\d+)$',                 'task'          ),
    url( r'^show_task$',            				 'show_task'     ),
    url( r'^change_status$',                         'change_status' ),
    url( r'^get_tasks$',                             'get_tasks'     ),
    url( r'^get_progress_bar_user/(?P<id_iterate>\d+)/(?P<id_user>\d+)$', 'get_progress_bar_user' ),
)