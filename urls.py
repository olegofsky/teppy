from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin

from source.employee.views import employee_list

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', employee_list, {'template_name': 'employee/employee_list.html'}),
    url(r'employee/', include('source.employee.urls')),

    url(r'^tests/', include('source.tests.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    (r'^accounts/login/$', login, {'template_name': 'login.html'}),
    (r'^accounts/logout/$', logout, {'template_name': 'logout.html'}),
    (r'^accounts/password_change/$', 'django.contrib.auth.views.password_change'),
    (r'^accounts/password_change/done/$', 'django.contrib.auth.views.password_change_done'),
)
