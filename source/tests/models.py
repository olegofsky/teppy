# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

PRIORITY_CHOICES = (
                    (1, 'low'),
                    (2, 'low-mid'),
                    (3, 'mid'),
                    (4, 'high-mid'),
                    (5, 'high'),
                    )

STATUS_CHOICES = (
                  (1, 'active'),
                  (2, 'not active'),
                  )

class TestSuit(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_NOT_ACTIVE = 'not active'

    STATUS_CHOICES = (
            (STATUS_ACTIVE, u'active'),
            (STATUS_NOT_ACTIVE, u'not active'),
    )

    QA_ID = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey(User, related_name='suits_author')
    producer = models.ForeignKey(User, related_name='suits_spec_author')

    overview = models.TextField()
    global_setup = models.TextField()

    spec = models.TextField()

    status = models.CharField(choices=STATUS_CHOICES, max_length=16)

    class Meta:
        verbose_name = 'Test suit'
        verbose_name_plural = 'Test suits'

    def __unicode__(self):
        return 'Test suit #{0}'.format(self.id)

    def as_html(self):
        return u'<span class="badge badge-info">{0}</span>'.format(self.__unicode__())

    def get_absolute_url(self):
        return '/tests/suit/{0}/'.format(self.id)

    def get_cases(self):
        return TestCase.objects.filter(suit=self)


class TestCase(models.Model):
    PRIORITY_LOW = 'low'
    PRIORITY_LOW_MID = 'low-mid'
    PRIORITY_MID = 'mid'
    PRIORITY_HIGH_MID = 'high-mid'
    PRIORITY_HIGH = 'high'

    PRIORITY_CHOICES = (
            (PRIORITY_LOW, u'low'),
            (PRIORITY_LOW_MID, u'low-mid'),
            (PRIORITY_MID, u'mid'),
            (PRIORITY_HIGH_MID, u'high-mid'),
            (PRIORITY_HIGH, u'high'),
    )

    STATUS_ACTIVE = 'active'
    STATUS_NOT_ACTIVE = 'not active'

    STATUS_CHOICES = (
            (STATUS_ACTIVE, u'active'),
            (STATUS_NOT_ACTIVE, u'not active'),
    )

    QA_ID = models.CharField(max_length=100, null=True, blank=True)

    author = models.ForeignKey(User, related_name='cases_author', verbose_name=u'Author')
    developer = models.ForeignKey(User, verbose_name=u'Developer')
    producer = models.ForeignKey(User, related_name='cases_spec_author', verbose_name=u'Producer')

    suit = models.ForeignKey(TestSuit, null=True, blank=True, verbose_name=u'Associated suit')

    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=16, verbose_name=u'Priority')

    setup = models.TextField(verbose_name=u'Setup')
    idea = models.TextField(verbose_name=u'Idea')
    procedure = models.TextField(verbose_name=u'Procedure')
    expected_result = models.TextField(verbose_name=u'Expected result')

    status = models.CharField(choices=STATUS_CHOICES, max_length=16, verbose_name=u'Status')

    date_created = models.DateTimeField(auto_now_add=True, verbose_name=u'Date created')
    date_modified = models.DateTimeField(auto_now=True, verbose_name=u'Date modidfied')

    class Meta:
        verbose_name = 'Test case'
        verbose_name_plural = 'Test cases'

    def __unicode__(self):
        return 'Test case #{0}'.format(self.id)

    def get_absolute_url(self):
        return '/tests/case/{0}/'.format(self.id)

    def get_bugs(self):
        return Bug.objects.filter(test_case=self)


class Bug(models.Model):
    QA_ID = models.CharField(max_length=100, null=True, blank=True)

    author = models.ForeignKey(User, related_name='bug_commiter')
    traceback = models.TextField(null=True, blank=True)
    test_case = models.ForeignKey(TestCase)

    date_opened = models.DateTimeField(auto_now_add=True)
    date_closed = models.DateTimeField(null=True, blank=True)

    gt = models.ForeignKey('GlobalTesting', null=True, blank=True)

    class Meta:
        verbose_name = 'Bug'
        verbose_name_plural = 'Bugs'

    def __unicode__(self):
        return 'Bug #{0}'.format(self.id)

    def get_absolute_url(self):
        return '/tests/bug/{0}/'.format(self.id)


class TestCaseInGT(models.Model):
    STATUS_PASSED = 'passed'
    STATUS_FAILED = 'failed'
    STATUS_QUEUED = 'queued'

    TC_STATUS_CHOICES = (
            (STATUS_PASSED, u'passed'),
            (STATUS_FAILED, u'failed'),
            (STATUS_QUEUED, u'queued'),
    )

    test_case = models.ForeignKey(TestCase)
    tester = models.ForeignKey(User, null=True, blank=True)
    gt = models.ForeignKey('GlobalTesting')
    status = models.CharField(choices=TC_STATUS_CHOICES, max_length=16, default='queued')

    def __unicode__(self):
        return 'Test case #{0} in general testing #{1}'.format(self.test_case.id, self.gt.id)

    def get_bugs(self):
        return Bug.objects.filter(gt=self.gt, test_case=self.test_case)


class GlobalTesting(models.Model):
    QA_ID = models.CharField(max_length=100, null=True, blank=True)

    author = models.ForeignKey(User, related_name='initiator')

    testers = models.ManyToManyField(User, related_name='members')

    test_cases = models.ManyToManyField(TestCase, through=TestCaseInGT)

    date_start = models.DateTimeField(null=True, blank=True)
    date_finish = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'GlobalTesting'
        verbose_name_plural = 'GlobalTestings'

    def __unicode__(self):
        return u'Global testing #{0}'.format(self.id)

    def get_absolute_url(self):
        return '/tests/gt/{0}'.format(self.id)
