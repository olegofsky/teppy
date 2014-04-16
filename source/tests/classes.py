# -*- coding: utf-8 -*-
from datetime import datetime

from source.tests.models import TestCaseInGT

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
        required_avg_speed = float(self.get_cases_count()) / self.get_seconds_remains()
        return required_avg_speed

    def get_avg_time_per_case(self):
        avg_time_per_case = u'N/A'
        if self.get_passed_cases_count():
            avg_time_per_case = float(self.get_elapsed_seconds()) / float(self.get_passed_cases_count())
        return avg_time_per_case

    def get_required_avg_time_per_case(self):
        required_avg_time_per_case = float(self.get_seconds_remains()) / float(self.get_cases_count())
        return required_avg_time_per_case

    def as_dict(self):
        return {
            'cases_count': self.get_cases_count(),
            'passed_cases_count': self.get_passed_cases_count(),
            'failed_cases_count': self.get_failed_cases_count(),
            'seconds_remains': self.get_seconds_remains(),
            'elapsed_seconds': self.get_elapsed_seconds(),
            'avg_speed': self.get_avg_speed(),
            'required_avg_speed': self.get_required_avg_speed(),
            'avg_time_per_case': self.get_avg_time_per_case(),
            'required_avg_time_per_case': self.get_required_avg_time_per_case()
        }
