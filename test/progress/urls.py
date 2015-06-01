from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testprogress.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',                       'progress.views.package_list',           name='package_list'),
    url(r'^add/$',                   'progress.views.package_add',            name='package_add'),
    url(r'^edit/(?P<pk>\d+)/$',      'progress.views.package_edit',           name='package_edit'),
    url(r'^delete/(?P<pk>\d+)/$',    'progress.views.package_delete',         name='package_delete'),
)
