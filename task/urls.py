from django.conf.urls import patterns, include, url

urlpatterns = patterns('task.views',

    url( r'^tasks$',                                 'show_tasks'       ),
    url( r'^dashboard$',                             'show_dashboard'   ),
    url( r'^task/$',            				     'task'             ),
    url( r'^task/(?P<id_task>\d+)$',                 'task'             ),
    url( r'^show_lst_not_dev$',            			 'show_lst_not_dev' ),
    url( r'^change_status$',                         'change_status'    ),
    url( r'^get_tasks$',                             'get_tasks'        ),
    url( r'^assign_for_user',                        'assign_for_user'  ),
    url( r'^get_progress_bar_user/(?P<id_iterate>\d+)/(?P<id_user>\d+)$', 'get_progress_bar_user' ),
)