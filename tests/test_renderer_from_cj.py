#!/usr/bin/env python
# encoding: utf-8


import tests.conftests
from collection_json import Collection, Data, Error, Item, Link, Query, Template
from django.conf.urls import patterns, url
from django.test import TestCase
from drf_collection_json.renderers import CollectionJSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


def reference_collection():
    """constructs a reference collection for testing"""
    link = Link("href_link", "rel_link")
    data = Data("data1", "value1")
    item = Item(href="href_item", data=[data], links=[link])
    error = Error(code=1, message="error text")
    query = Query("href_query", "rel", data=[data])
    template = Template(data=[data])
    collection = Collection(href="href_collection",
                            links=[link],
                            items=[item],
                            queries=[query],
                            template=template,
                            error=error)
    return collection


class CollectionJSONTest(TestCase):
    """tests when the response contains a collection+json object"""
    urls = __name__

    def test_no_serializer_view(self):
        """tests that the collection json serializer doesn't throw any
        errors when missing a serializer class"""
        self.client.get("/noserializer")

    def test_collection_equality(self):
        """tests that a collection is sent properly through the serializer"""
        response = self.client.get("/collection")
        expected = reference_collection()
        content = response.content.decode("utf-8")
        actual = Collection.from_json(content)
        self.assertEqual(actual, expected)


# various views for tests
class NoSerializerView(APIView):
    renderer_classes = (CollectionJSONRenderer,)

    def get(self, request):
        collection = Collection(href="")
        return Response(collection)


class CollectionView(APIView):
    renderer_classes = (CollectionJSONRenderer,)

    def get(self, request):
        return Response(reference_collection())


# url patterns for tests
urlpatterns = patterns(
    '',
    url(r'^noserializer$', NoSerializerView.as_view()),
    url(r'^collection$', CollectionView.as_view()),
)
