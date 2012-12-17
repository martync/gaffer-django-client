from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('gafferclient.views',
    url(r'^$', 'process_list', name='process_list'),
    url(r'^process/([^/]+)/$', 'process_detail', name='process_detail'),
    url(r'^process/([^/]+)/num_add/$', 'process_set', {'action': 'add'}, name='process_num_add'),
    url(r'^process/([^/]+)/num_sub/$', 'process_set', {'action': 'sub'}, name='process_num_sub'),
    url(r'^process/([^/]+)/stop/$', 'process_set', {'action': 'stop'}, name='process_stop'),
    url(r'^process/([^/]+)/start/$', 'process_set', {'action': 'start'}, name='process_start'),
    url(r'^process/([^/]+)/restart/$', 'process_set', {'action': 'restart'}, name='process_restart'),


    url(r'^pid/$', 'pid_list', name='pid_list'),
    url(r'^([^/]+)/pid/([0-9^/]+)/$', 'pid_detail', name='pid_detail'),
    url(r'^([^/]+)/pid/([0-9^/]+)/stop/$', 'pid_stop', name='pid_stop'),


)
