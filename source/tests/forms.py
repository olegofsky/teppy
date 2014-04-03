# -*- coding: utf-8 -*-
from django import forms
from source.tests import models

class TestCaseForm(forms.ModelForm):

    class Meta:
        model = models.TestCase
        exclude = ('QA_ID', 'status')


class SuitAddForm(forms.ModelForm):

    class Meta:
        model = models.TestSuit
        exclude = ('QA_ID', 'status')


class BugAddForm(forms.ModelForm):

    class Meta:
        model = models.Bug
        exclude = ('QA_ID')

class GlobalTestingAddForm(forms.ModelForm):

    class Meta:
        model = models.GlobalTesting
