#!/usr/bin/env python
# encoding: utf-8


import tests.conftests
from collection_json import Collection
from django.conf.urls import patterns, url
from django.test import TestCase
from drf_collection_json.renderers import CollectionJSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


class CollectionJSONTest(TestCase):
    """tests when the response contains a collection+json object"""
    urls = __name__

    def test_no_serializer_view(self):
        self.client.get("/noserializer")


# various views for tests
class NoSerializerView(APIView):
    renderer_classes = (CollectionJSONRenderer,)

    def get(self, request):
        collection = Collection(href="")
        return Response(collection)

# url patterns for tests
urlpatterns = patterns(
    '',
    url(r'^noserializer$', NoSerializerView.as_view()),
)
