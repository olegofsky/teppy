# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.conf.urls.defaults import url, patterns
from django.views.generic import ListView, DetailView

from source.tests import views
from source.tests.models import TestCase, TestSuit, Bug, GlobalTesting

urlpatterns = patterns('',
        url(r'^suit/$', login_required(ListView.as_view(model=TestSuit))),
        url(r'^suit/(?P<pk>\d+)/$', login_required(DetailView.as_view(model=TestSuit))),
        url(r'^suit/add/', views.TestSuitCreate.as_view()),
        url(r'^suit/(?P<pk>\d+)/$', views.TestSuitUpdate.as_view()),
        url(r'^suit/(?P<pk>\d+)/delete/$', views.TestSuitDelete.as_view()),

        url(r'^case/$', login_required(ListView.as_view(model=TestCase))),
        url(r'^case/(?P<pk>\d+)/$', login_required(DetailView.as_view(model=TestCase))),
        url(r'^case/add/', views.TestCaseCreate.as_view()),
        url(r'^case/(?P<pk>\d+)/$', views.TestCaseUpdate.as_view()),
        url(r'^case/(?P<pk>\d+)/delete/$', views.TestCaseDelete.as_view()),

        url(r'^bug/$', login_required(ListView.as_view(model=Bug))),
        url(r'^bug/(?P<pk>\d+)/$', login_required(DetailView.as_view(model=Bug))),
        url(r'^bug/add/$', views.BugCreate.as_view()),
        url(r'^bug/add/(?P<test_case_id>\d+)/$', views.BugCreate.as_view()),
        url(r'^bug/add/(?P<test_case_id>\d+)/(?P<gt_id>\d+)/$', views.BugCreate.as_view()),

        url(r'^gt/$', login_required(ListView.as_view(model=GlobalTesting))),
        url(r'^gt/add/$', views.GTCreate.as_view()),
        url(r'^gt/(?P<pk>\d+)/$', views.GTDetails.as_view()),

        url(r'^pick_up_case_in_gt/(?P<tcigt_id>\d+)/$', views.assign_case_in_gt),
        url(r'^assign_case_in_gt/(?P<tcigt_id>\d+)/(?P<user_id>\d+)/$', views.assign_case_in_gt),
        url(r'^pass_case_in_gt/(?P<tcigt_id>\d+)/$', views.pass_case_in_gt),
)
