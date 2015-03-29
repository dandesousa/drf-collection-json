#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import patterns, url
from testapp.cj_views import NoSerializerCJView
from testapp.cj_views import CollectionCJView
from testapp.infer_views import NoSerializerView as NoSerializerInferView
from testapp.infer_views import PersonView as PersonInferView


urlpatterns = patterns(
    '',
    url(r'cj/noserializer', NoSerializerCJView.as_view()),
    url(r'cj/collection', CollectionCJView.as_view()),
    url(r'infer/noserializer', NoSerializerInferView.as_view()),
    url(r'infer/person', PersonInferView.as_view())
)
