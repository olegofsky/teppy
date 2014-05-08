# -*- coding: utf-8 -*-
from django.contrib.auth.models import User

from rest_framework import serializers, viewsets, routers

from source.tests.models import TestCase, TestSuit, Bug, GlobalTesting


class TestCaseSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = TestCase


class TestCaseViewSet(viewsets.ModelViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer


class TestSuitSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = TestSuit


class TestSuitViewSet(viewsets.ModelViewSet):
    queryset = TestSuit.objects.all()
    serializer_class = TestSuitSerializer


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BugSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Bug


class BugViewSet(viewsets.ModelViewSet):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer


class GlobalTestingSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = GlobalTesting


class GlobalTestingViewSet(viewsets.ModelViewSet):
    queryset = GlobalTesting.objects.all()
    serializer_class = GlobalTestingSerializer


router = routers.DefaultRouter()
router.register(r'testcases', TestCaseViewSet)
router.register(r'testsuits', TestSuitViewSet)
router.register(r'users', UserViewSet)
router.register(r'bugs', BugViewSet)
router.register(r'globaltestings', GlobalTestingViewSet)