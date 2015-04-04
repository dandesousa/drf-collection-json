#!/usr/bin/env python
# encoding: utf-8


from drf_collection_json.renderers import CollectionJSONRenderer
from rest_framework.views import APIView
from rest_framework import viewsets
from testapp.models import Person
from testapp.serializers import PersonSerializer
from rest_framework.response import Response


class NoSerializerView(APIView):
    renderer_classes = (CollectionJSONRenderer,)

    def get(self, request):
        return Response()


class PersonViewSet(viewsets.ModelViewSet):
    renderer_classes = (CollectionJSONRenderer,)
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
