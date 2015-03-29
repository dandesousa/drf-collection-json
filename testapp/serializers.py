#!/usr/bin/env python
# encoding: utf-8

from rest_framework import serializers
from testapp.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
