# -*- coding: utf-8 -*-
from django.conf.urls.defaults import url, patterns
from source.tests.views import *

from source.employee import views

urlpatterns = patterns('',
                       url(r'^$', views.employee_list, {'template_name': 'employee/employee_list.html'}),
                       url(r'^employee/(?P<employee_id>\d+)/$', views.employee_details, {'template_name': 'employee/employee_details.html'}),
)
