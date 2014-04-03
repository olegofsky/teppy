# -*- coding: utf-8 -*-
from django.contrib import admin
from source.tests.models import TestCase, TestSuit, TestCaseInGT, GlobalTesting, Bug

class TestCaseAdmin(admin.ModelAdmin):
    pass

class TestSuitAdmin(admin.ModelAdmin):
    pass

class TestCaseInGTAdmin(admin.ModelAdmin):
    pass

class GlobalTestingAdmin(admin.ModelAdmin):
    pass

class BugAdmin(admin.ModelAdmin):
    pass

admin.site.register(TestCase, TestCaseAdmin)
admin.site.register(TestSuit, TestSuitAdmin)
admin.site.register(TestCaseInGT, TestCaseInGTAdmin)
admin.site.register(GlobalTesting, GlobalTestingAdmin)
admin.site.register(Bug, BugAdmin)
