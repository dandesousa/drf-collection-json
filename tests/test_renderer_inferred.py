#!/usr/bin/env python
# encoding: utf-8


import tests.conftests
from django.conf.urls import patterns, url
from django.test import TestCase
from drf_collection_json.renderers import CollectionJSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


class DictionaryTest(TestCase):
    """tests when the response contains a dictionary"""
    urls = __name__

    def test_no_serializer_view(self):
        with self.assertRaises(TypeError):
            self.client.get("/noserializer")


class ListTest(TestCase):
    """tests when the response contains a list"""
    urls = __name__


# various views for tests
class NoSerializerView(APIView):
    renderer_classes = (CollectionJSONRenderer,)

    def get(self, request):
        return Response()


# url patterns for tests
urlpatterns = patterns(
    '',
    url(r'^noserializer$', NoSerializerView.as_view()),
)
