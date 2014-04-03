# -*- coding: utf-8 -*-
from django.conf.urls.defaults import url, patterns
from source.tests import views

urlpatterns = patterns('',
                        url(r'^suit/$', views.suit_list, {'template_name': 'tests/suit_list.html'}),
                        url(r'^suit/add/', views.suit_add, {'template_name': 'tests/suit_add.html'}),
                        url(r'^suit/(?P<suit_id>\d+)/$', views.suit_details, {'template_name': 'tests/suit_details.html'}),

                        url(r'^case/$', views.case_list, {'template_name': 'tests/case_list.html'}),
                        url(r'^case/add/', views.case_add, {'template_name': 'tests/case_add.html'}),
                        url(r'^case/(?P<case_id>\d+)/$', views.case_details, {'template_name': 'tests/case_details.html'}),

                        url(r'^bug/$', views.bug_list, {'template_name': 'tests/bug_list.html'}),
                        url(r'^bug/add/$', views.bug_add, {'template_name': 'tests/bug_add.html'}),
                        url(r'^bug/add/(?P<tcigt_id>\d+)/$', views.bug_add, {'template_name': 'tests/bug_add.html'}),
                        url(r'^bug/(?P<bug_id>\d+)/$', views.bug_details, {'template_name': 'tests/bug_details.html'}),

                        url(r'^gt/$', views.gt_list, {'template_name': 'tests/gt_list.html'}),
                        url(r'^gt/add/', views.gt_add, {'template_name': 'tests/gt_add.html'}),
                        url(r'^gt/(?P<gt_id>\d+)/$', views.gt_details, {'template_name': 'tests/gt_details.html'}),
                        url(r'^pick_up_case_in_gt/(?P<tcigt_id>\d+)/$', views.assign_case_in_gt),
                        url(r'^assign_case_in_gt/(?P<tcigt_id>\d+)/(?P<user_id>\d+)/$', views.assign_case_in_gt),
                        url(r'^pass_case_in_gt/(?P<tcigt_id>\d+)/$', views.pass_case_in_gt),
)
