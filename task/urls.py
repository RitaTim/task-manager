from django.conf.urls import patterns, include, url

urlpatterns = patterns('task.views',

    url( r'^tasks/(?P<id_project>\d+)$',             'show_tasks'    ),
    url( r'^dashboard/(?P<id_project>\d+)$',         'show_dashboard'),
    url( r'^edit_task$',            				 'edit_task'     ),
    url( r'^edit_task/(?P<id_task>\d+)$',            'edit_task'     ),
    url( r'^change_status$',                         'change_status' ),
    url( r'^get_tasks$',                             'get_tasks'     ),
)