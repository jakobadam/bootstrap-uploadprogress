from django.conf.urls import url

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'testprogress.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',                       views.package_list,           name='package_list'),
    url(r'^add/$',                   views.package_add,            name='package_add'),
    url(r'^edit/(?P<pk>\d+)/$',      views.package_edit,           name='package_edit'),
    url(r'^delete/(?P<pk>\d+)/$',    views.package_delete,         name='package_delete'),
]
