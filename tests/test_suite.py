#!/usr/bin/env python
# encoding: utf-8


import tests.conftests
from django.test import TestCase
import unittest


class InvalidClientTest(TestCase):
    urls = "tests.urls"

    def test_no_serializer_view(self):
        with self.assertRaises(TypeError):
            self.client.get("/noserializer")


if __name__ == "__main__":
    unittest.main()
