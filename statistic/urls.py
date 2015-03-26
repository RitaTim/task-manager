from django.conf.urls import patterns, include, url

urlpatterns = patterns('statistic.views',
    url( r'^$',                   'statistic_users'    ),
    url( r'^get_progress_users$', 'get_progress_users' ),
    url( r'^get_data_graphic$',   'get_data_graphic'   ),
)