#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import patterns, url
from testapp.cj_views import NoSerializerCJView
from testapp.cj_views import CollectionCJView
from testapp.infer_views import NoSerializerView as NoSerializerInferView
from testapp.infer_views import PersonViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = patterns(
    '',
    url(r'cj/noserializer', NoSerializerCJView.as_view()),
    url(r'cj/collection', CollectionCJView.as_view()),
    url(r'infer/noserializer', NoSerializerInferView.as_view()),
)

router = DefaultRouter()
router.register(r'infer/person', PersonViewSet)
urlpatterns += router.urls
