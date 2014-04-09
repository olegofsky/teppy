# -*- coding: utf-8 -*-
from django.conf.urls.defaults import url, patterns
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from source.tests.views import *

urlpatterns = patterns('',
       url(r'^$', login_required(ListView.as_view(model=User))),
       url(r'^employee/(?P<pk>\d+)/$', login_required(DetailView.as_view(model=User))),
)
