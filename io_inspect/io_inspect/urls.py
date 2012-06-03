from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^io_inspect/$', 'checklist.views.index'),
    (r'^io_inspect/(?P<Check_id>\d+)/$', 'checklist.views.detail'),
    (r'^io_inspect/(?P<Check_id>\d+)/results/$', 'checklist.views.results'),
    (r'^io_inspect/(?P<Check_id>\d+)vote/$', 'checklist.views.vote'),
	# Examples:
    # url(r'^$', 'io_inspect.views.home', name='home'),
    # url(r'^io_inspect/', include('io_inspect.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
