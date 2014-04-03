# -*- coding: utf-8 -*-
from django.contrib import admin
from source.tests.models import Test_Case, Test_Suit, TestCaseInGT, GlobalTesting, Bug

class Test_Case_Admin(admin.ModelAdmin):
    pass

class Test_Suit_Admin(admin.ModelAdmin):
    pass

class TestCaseInGT_Admin(admin.ModelAdmin):
    pass

class GlobalTesting_Admin(admin.ModelAdmin):
    pass

class Bug_Admin(admin.ModelAdmin):
    pass

admin.site.register(Test_Case, Test_Case_Admin)
admin.site.register(Test_Suit, Test_Suit_Admin)
admin.site.register(TestCaseInGT, TestCaseInGT_Admin)
admin.site.register(GlobalTesting, GlobalTesting_Admin)
admin.site.register(Bug, Bug_Admin)
