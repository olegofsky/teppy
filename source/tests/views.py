# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

from django.views.generic import ListView, DetailView

from source.tests.classes import GTValues
from source.tests.models import TestCase, TestSuit, Bug, GlobalTesting, TestCaseInGT
from source.tests.forms import TestCaseForm, SuitAddForm, BugAddForm, GlobalTestingAddForm


class CaseList(ListView):
    model = TestCase

class CaseDetail(DetailView):
    model = TestCase

@login_required
def case_list(request, template_name):
    context = RequestContext(request)
    context['cases'] = TestCase.objects.all()
    return render_to_response(template_name, context)

@login_required
def suit_list(request, template_name):
    context = RequestContext(request)
    context['suits'] = TestSuit.objects.all()
    return render_to_response(template_name, context)

@login_required
def case_details(request, template_name, case_id):
    context = RequestContext(request)
    context['case'] = TestCase.objects.get(id=case_id)
    return render_to_response(template_name, context)

@login_required
def suit_details(request, template_name, suit_id):
    context = RequestContext(request)
    context['suit'] = TestSuit.objects.get(id=suit_id)
    return render_to_response(template_name, context)

@login_required
def case_add(request, template_name):
    context = RequestContext(request)
    if request.method == 'POST':
        data = TestCaseForm(request.POST)
        if data.is_valid():
            case = data.save(commit=False)
            case.status = TestCase.STATUS_ACTIVE
            case.save()
            return HttpResponseRedirect(case.get_absolute_url())
        else:
            context['form'] = TestCaseForm(request.POST)
            return render_to_response(template_name, context)
    else:
        form_kwargs = {
                        'author': request.user,
                        'priority': TestCase.PRIORITY_MID,
                    }
        if 'based_on' in request.GET:
            form_kwargs['suit'] = TestSuit.objects.get(id=request.GET['based_on'])

        context['form'] = TestCaseForm(initial=form_kwargs)
        return render_to_response(template_name, context)

@login_required
def suit_add(request, template_name):
    context = RequestContext(request)
    if request.method == 'POST':
        data = SuitAddForm(request.POST)
        if data.is_valid():
            suit = data.save(commit=False)
            suit.status = TestSuit.STATUS_ACTIVE
            suit.save()
            return HttpResponseRedirect(suit.get_absolute_url())
        else:
            context['form'] = SuitAddForm(request.POST)
            return render_to_response(template_name, context)
    else:
        context['form'] = SuitAddForm(initial={'author': request.user})
        return render_to_response(template_name, context)

@login_required
def bug_list(request, template_name):
    context = RequestContext(request)
    context['bugs'] = Bug.objects.all()
    return render_to_response(template_name, context)

@login_required
def bug_add(request, template_name, tcigt_id=None):
    context = RequestContext(request)
    tcigt = None
    if tcigt_id:
        tcigt = TestCaseInGT.objects.get(id=tcigt_id)

    if request.method == 'POST':
        data = BugAddForm(request.POST)
        if data.is_valid():
            bug = data.save()
            if tcigt:
                bug.gt = tcigt.gt
                bug.test_case = tcigt.test_case
                bug.save()

                return HttpResponseRedirect(tcigt.gt.get_absolute_url())

            return HttpResponseRedirect(bug.get_absolute_url())
        else:
            context['form'] = BugAddForm(request.POST)
            return render_to_response(template_name, context)
    else:
        form_kwargs = {'author': request.user}
        if tcigt:
            form_kwargs['gt'] = tcigt.gt
            form_kwargs['test_case'] = tcigt.test_case

        context['form'] = BugAddForm(initial=form_kwargs)
    return render_to_response(template_name, context)

@login_required
def bug_details(request, template_name, bug_id):
    context = RequestContext(request)
    context['bug'] = Bug.objects.get(id=bug_id)
    return render_to_response(template_name, context)

@login_required
def gt_list(request, template_name):
    context = RequestContext(request)
    context['gts'] = GlobalTesting.objects.all()
    return render_to_response(template_name, context)

@login_required
def gt_details(request, template_name, gt_id):
    context = RequestContext(request)
    gt = GlobalTesting.objects.get(id=gt_id)
    context['gt'] = gt
    context['gt_tests'] = TestCaseInGT.objects.filter(gt=gt)
    context['gtvalues'] = GTValues(gt)
    return render_to_response(template_name, context)

@login_required
def gt_add(request, template_name):
    context = RequestContext(request)
    if request.method == 'POST':
        data = GlobalTestingAddForm(request.POST)
        if data.is_valid():
            gt = data.save(commit=False)
            gt.save()
            for case_id in request.POST.getlist('test_cases'):
                TestCaseInGT.objects.create(test_case_id=case_id, gt=gt)
            for tester_id in request.POST.getlist('testers'):
                gt.testers.add(User.objects.get(id=tester_id))
            return HttpResponseRedirect(gt.get_absolute_url())
        else:
            context['form'] = GlobalTestingAddForm(request.POST)
            return render_to_response(template_name, context)
    else:
        context['form'] = GlobalTestingAddForm(initial={'author': request.user})
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
