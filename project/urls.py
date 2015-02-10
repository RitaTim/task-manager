from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'task_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'project.views.projects'),
    url(r'^create$', 'project.views.create'),
    url(r'^new$', 'project.views.new'),
    url(r'^project/(?P<id_project>\d+)$', 'project.views.show_project'),
)