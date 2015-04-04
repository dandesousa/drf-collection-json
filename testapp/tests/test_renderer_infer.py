#!/usr/bin/env python
# encoding: utf-8

from django.test import TestCase
from collection_json import Collection
from testapp.models import Person

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse


class DictionaryTest(TestCase):
    """tests when the response contains a dictionary"""

    def test_no_serializer_view(self):
        with self.assertRaises(TypeError):
            self.client.get("/infer/noserializer")


class PersonTest(TestCase):

    def setUp(self):
        self.num_people = 10
        for i in range(self.num_people):
            p = Person.objects.create(name="person{}".format(i),
                                      address="address{}".format(i))
            p.save()
        self.url = "/infer/person/"
        response = self.client.get(self.url)
        content = response.content.decode("utf-8")
        self.collection = Collection.from_json(content)

    def test_db_setup(self):
        """asserts that the database was properly initialized"""
        self.assertEqual(self.num_people, len(Person.objects.all()))

    def test_collection_items(self):
        """asserts that the right number of items was parsed"""
        self.assertEqual(self.num_people, len(self.collection.items))

    def test_collection_names(self):
        """tests that the given attribute was parsed correctly"""
        for i, item in enumerate(self.collection.items):
            expected = "person{}".format(i)
            self.assertEqual(item.name.value, expected)

    def test_collection_address(self):
        """tests that the given attribute was parsed correctly"""
        for i, item in enumerate(self.collection.items):
            expected = "address{}".format(i)
            self.assertEqual(item.address.value, expected)

    def test_collection_identity_link(self):
        """tests that the href for the collection is correct"""
        actual = urlparse(self.collection.href).path
        self.assertEqual(actual, self.url)

    def test_collection_item_identity_link(self):
        """tests that the href for collection item its is correct"""
        # it should be None, its just a list view, nothing to link against.
        for i, item in enumerate(self.collection.items):
            expected = "{}{}/".format(self.url, i+1)
            actual = urlparse(item.href).path
            self.assertEqual(actual, expected)


class ListTest(TestCase):
    """tests when the response contains a list"""
    urls = "testapp.urls"
