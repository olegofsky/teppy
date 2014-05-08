from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from source.tests.rest_api import router

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', employee_list, {'template_name': 'auth/user_list.html'}),
    url(r'^$', login_required(ListView.as_view(model=User))),
    url(r'employee/', include('source.employee.urls')),

    url(r'^tests/', include('source.tests.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    (r'^accounts/login/$', login, {'template_name': 'login.html'}),
    (r'^accounts/logout/$', logout, {'template_name': 'logout.html'}),
    (r'^accounts/password_change/$', 'django.contrib.auth.views.password_change'),
    (r'^accounts/password_change/done/$', 'django.contrib.auth.views.password_change_done'),

    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^restful/', include(router.urls)),
)
