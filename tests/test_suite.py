#!/usr/bin/env python
# encoding: utf-8


import tests.conftests
from collection_json import Collection
from django.conf.urls import patterns, url
from django.test import TestCase
from drf_collection_json.renderers import CollectionJSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


class DictionaryTest(TestCase):
    """tests when the response contains a dictionary"""
    urls = "tests.test_suite"

    def test_no_serializer_view(self):
        with self.assertRaises(TypeError):
            self.client.get("/noserializer")


class ListTest(TestCase):
    """tests when the response contains a list"""
    urls = "tests.test_suite"


class CollectionJSONTest(TestCase):
    """tests when the response contains a collection+json object"""
    urls = "tests.test_suite"

    def test_no_serializer_view(self):
        self.client.get("/noserializer/cj")


# various views for tests
class NoSerializerView(APIView):
    renderer_classes = (CollectionJSONRenderer,)

    def get(self, request):
        return Response()


class NoSerializerCjView(APIView):
    renderer_classes = (CollectionJSONRenderer,)

    def get(self, request):
        collection = Collection(href="")
        return Response(collection)

# url patterns for tests
urlpatterns = patterns(
    '',
    url(r'^noserializer$', NoSerializerView.as_view()),
    url(r'^noserializer/cj$', NoSerializerCjView.as_view()),
)
