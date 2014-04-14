# -*- coding: utf-8 -*-
from datetime import datetime
import json
from django.http import HttpResponse

from source.tests.models import TestCaseInGT, GlobalTesting

class GTValues(object):
    def __init__(self, gt):
        self.gt = gt

    def get_cases_count(self):
        return self.gt.test_cases.all().count()

    def get_passed_cases_count(self):
        return self.gt.testcaseingt_set.filter(status=TestCaseInGT.STATUS_PASSED).count()

    def get_failed_cases_count(self):
        return self.gt.testcaseingt_set.filter(status=TestCaseInGT.STATUS_FAILED).count()

    def get_seconds_remains(self):
        if self.gt.date_finish > datetime.now():
            return (self.gt.date_finish - datetime.now()).seconds
        else:
            return -(datetime.now() - self.gt.date_finish).seconds

    def get_elapsed_seconds(self):
        return (datetime.now() - self.gt.date_start).seconds

    def get_avg_speed(self):
        avg_speed = u'N/A'
        if self.get_passed_cases_count():
            avg_speed = float(self.get_passed_cases_count()) / self.get_elapsed_seconds()
        return avg_speed

    def get_required_avg_speed(self):
        return u'N/A'


def gt_params(request, gt_id):
    gt = GlobalTesting.objects.get(id=1)
    gt_values = GTValues(gt)
    return HttpResponse(json.dumps({
        'cases_count': gt_values.get_cases_count(),
        'passed_cases_count': gt_values.get_passed_cases_count(),
        'failed_cases_count': gt_values.get_failed_cases_count(),
        'seconds_remains': gt_values.get_seconds_remains(),
        'elapsed_seconds': gt_values.get_elapsed_seconds(),
        'avg_speed': gt_values.get_avg_speed(),
        'required_avg_speed': gt_values.get_required_avg_speed(),
    }))
