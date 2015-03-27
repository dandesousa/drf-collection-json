#!/usr/bin/env python
# encoding: utf-8


import tests.conftests
from django.conf.urls import patterns, url, include
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_collection_json.renderers import CollectionJSONRenderer


class NoSerializerView(APIView):
    renderer_classes = (CollectionJSONRenderer,)

    def get(self, request):
        return Response()


urlpatterns = patterns(
    '',
    url(r'^noserializer$', NoSerializerView.as_view()),
)
