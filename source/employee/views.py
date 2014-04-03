# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.template.context import RequestContext
from django.shortcuts import render_to_response

def employee_list(request, template_name):
    context = RequestContext(request)
    context['employees'] = User.objects.all()
    return render_to_response(template_name, context)

def employee_details(request, template_name, employee_id):
    context = RequestContext(request)
    context['employee'] = User.objects.get(id=employee_id)
    return render_to_response(template_name, context)
