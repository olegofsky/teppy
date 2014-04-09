# -*- coding: utf-8 -*-
from datetime import datetime

from source.tests.models import TestCaseInGT

class GTValues(object):
    def __init__(self, gt):
        cases_count = gt.test_cases.all().count()
        self.cases_count = cases_count
        passed_cases_count = gt.test_cases.filter(status=TestCaseInGT.STATUS_PASSED).count()
        self.passed_cases_count = passed_cases_count
        self.failed_cases_count = gt.test_cases.filter(status=TestCaseInGT.STATUS_FAILED).count()

        self.time_remains = 'N/A'
        self.avg_speed = 'N/A'
        self.required_avg_speed = 'N/A'
'''
        if gt.date_finish:
            time_remains = gt.date_finish - datetime.now()
            self.time_remains = time_remains
            if time_remains.minutes:
                self.required_avg_speed = (cases_count - passed_cases_count) / time_remains.minutes

        if gt.date_start:
            time_left = datetime.now() - gt.date_start
            minutes_left = time_left.seconds / 60
            if minutes_left:
                self.avg_speed = passed_cases_count / minutes_left
'''