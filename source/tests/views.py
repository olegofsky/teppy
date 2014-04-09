# -*- coding: utf-8 -*-
from datetime import datetime

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

from source.tests.classes import GTValues
from source.tests.models import TestCase, TestSuit, GlobalTesting, TestCaseInGT, Bug
from source.tests.forms import BugForm, GlobalTestingForm, TestSuitForm, TestCaseForm

from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

class LoginReqiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(type(self), self).dispatch(*args, **kwargs)

class TestCaseCreate(CreateView):
    model = TestCase
    form_class = TestCaseForm

    def get_initial(self):
        initial_kwargs = {
            'author': self.request.user,
            'priority': TestCase.PRIORITY_MID,
        }
        if 'based_on' in self.request.GET:
            initial_kwargs['suit'] = TestSuit.objects.get(id=self.request.GET['based_on'])
        return initial_kwargs

    def form_valid(self, form):
        form.instance.status = TestCase.STATUS_ACTIVE
        return super(TestCaseCreate, self).form_valid(form)


class TestCaseUpdate(UpdateView):
    model = TestCase


class TestCaseDelete(DeleteView):
    model = TestCase


class TestSuitCreate(CreateView):
    model = TestSuit
    form_class = TestSuitForm

    def get_initial(self):
        return {'author': self.request.user}

    def form_valid(self, form):
        form.instance.status = TestSuit.STATUS_ACTIVE
        return super(TestSuitCreate, self).form_valid(form)


class TestSuitUpdate(UpdateView):
    model = TestSuit


class TestSuitDelete(DeleteView):
    model = TestSuit


class BugCreate(CreateView):
    model = Bug
    form_class = BugForm

    def get_initial(self, **kwargs):
        form_kwargs = {'author': self.request.user}
        if 'test_case_id' in self.kwargs and self.kwargs['test_case_id']:
            test_case = TestCase.objects.get(id=self.kwargs['test_case_id'])
            form_kwargs['test_case'] = test_case
        return form_kwargs

    def form_valid(self, form):
        return super(BugCreate, self).form_valid(form)


class BugUpdate(UpdateView):
    model = Bug


class BugDelete(DeleteView):
    model = Bug


class GTCreate(CreateView):
    model = GlobalTesting
    form_class = GlobalTestingForm

    def get_initial(self):
        return {
                'author': self.request.user,
                'date_start': datetime.now(),
                'date_finish': datetime.now(),
            }

    def form_valid(self, form):
        generaltesting = form.save()
        for case_id in self.request.POST.getlist('test_cases'):
            TestCaseInGT.objects.create(test_case_id=case_id, gt=generaltesting)

        for tester_id in self.request.POST.getlist('testerts'):
            generaltesting.testers.add(User.objects.get(id=tester_id))

        generaltesting.save()
        return super(GTCreate, self).form_valid(form)


class GTDetails(DetailView):
    model = GlobalTesting

    def get_context_data(self, **kwargs):
        context = super(GTDetails, self).get_context_data(**kwargs)
        gt = GlobalTesting(id=self.kwargs['pk'])
        context['gt_tests'] = TestCaseInGT.objects.filter(gt=self.kwargs['pk'])
        context['gtvalues'] = GTValues(gt)
        return context

@login_required
def gt_add(request, template_name):
    context = RequestContext(request)
    if request.method == 'POST':
        data = GlobalTestingForm(request.POST)
        if data.is_valid():
            gt = data.save(commit=False)
            gt.save()
            for case_id in request.POST.getlist('test_cases'):
                TestCaseInGT.objects.create(test_case_id=case_id, gt=gt)
            for tester_id in request.POST.getlist('testers'):
                gt.testers.add(User.objects.get(id=tester_id))
            return HttpResponseRedirect(gt.get_absolute_url())
        else:
            context['form'] = GlobalTestingForm(request.POST)
            return render_to_response(template_name, context)
    else:
        context['form'] = GlobalTestingForm(
            initial={
                'author': request.user,
                'date_start': datetime.now(),
                'date_finish': datetime.now(),
            })
    return render_to_response(template_name, context)

@login_required
def assign_case_in_gt(request, tcigt_id, user_id=None):
    if user_id:
        user = User.objects.get(id=user_id)
    else:
        user = request.user
    tcigt = TestCaseInGT.objects.get(id=tcigt_id)
    tcigt.tester = user
    tcigt.save()
    return HttpResponseRedirect(tcigt.gt.get_absolute_url())

@login_required
def pass_case_in_gt(request, tcigt_id):
    tcigt = TestCaseInGT.objects.get(id=tcigt_id)
    tcigt.status = TestCaseInGT.STATUS_PASSED
    tcigt.save()
    return HttpResponseRedirect(tcigt.gt.get_absolute_url())
