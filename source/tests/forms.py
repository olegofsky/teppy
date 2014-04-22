# -*- coding: utf-8 -*-
from django import forms
from source.tests import models

class TestCaseForm(forms.ModelForm):

    class Meta:
        model = models.TestCase
        exclude = ('QA_ID', 'status')


class TestSuitForm(forms.ModelForm):

    class Meta:
        model = models.TestSuit
        exclude = ('QA_ID', 'status')


class BugForm(forms.ModelForm):

    class Meta:
        model = models.Bug
        exclude = ('QA_ID', )

class GlobalTestingForm(forms.ModelForm):

    class Meta:
        model = models.GlobalTesting
