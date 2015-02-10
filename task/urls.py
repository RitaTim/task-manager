from django.conf.urls import patterns, include, url

urlpatterns = patterns('task.views',
    # Examples:
    # url(r'^$', 'task_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', 'project.views.projects'),
    #url(r'^create$', 'project.views.create'),
    url(r'^new/(?P<id_project>\d+)$', 'new'),
    url(r'^tasks/(?P<id_project>\d+)$', 'show_tasks'),
    url(r'^tasks/(?P<id_project>\d+)/change_order$', 'change_order'),
    url(r'^tasks/(?P<id_project>\d+)/(?P<sort_by>\w+)$', 'show_tasks'),
    url(r'^dashboard/(?P<id_project>\d+)$', 'show_dashboard'),
    url(r'^get_tasks$', 'get_tasks'),
    #url(r'^dashboard/(?P<id_project>\d+)/(?P<id_iteration>\d+)$', 'show_dashboard'),
    #url(r'^dashboard/(?P<id_project>\d+)/(?P<id_iteration>\d+)/(?P<id_user>\d+)$', 'show_dashboard'),
    #url(r'^project/(?P<id_project>\d+)$', 'project.views.show_project'),
)