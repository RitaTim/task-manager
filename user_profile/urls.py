from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'task_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'user_profile.views.profile'),
    url(r'^dashboard$', 'user_profile.views.dashboard'),
    url(r'^dashboard/(?P<id_project>\d+)$', 'user_profile.views.dashboard'),
 	url(r'^dashboard_change$', 'user_profile.views.dashboard_change'),   
)