# -*- coding: utf-8 -*-
from django import forms
from source.tests import models

class CaseAddForm(forms.ModelForm):

    class Meta:
        model = models.Test_Case
        exclude = ('QA_ID', 'status')


class SuitAddForm(forms.ModelForm):

    class Meta:
        model = models.Test_Suit
        exclude = ('QA_ID', 'status')


class BugAddForm(forms.ModelForm):

    class Meta:
        model = models.Bug
        exclude = ('QA_ID')

class GlobalTestingAddForm(forms.ModelForm):

    class Meta:
        model = models.GlobalTesting
