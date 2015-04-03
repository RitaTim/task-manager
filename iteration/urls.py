from django.conf.urls import patterns, include, url

urlpatterns = patterns('iteration.views',
    url( r'^$',                            'iterates' ),
    url( r'^set_iterate_days$',    'set_iterate_days' ),
    url( r'^iterate/$',                    'iterate'  ),
    url( r'^iterate/(?P<iterate_id>\d+)$', 'iterate'  ),
)