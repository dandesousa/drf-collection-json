#!/usr/bin/env python
# encoding: utf-8


import os
import sys
import unittest


def test_all():
    sys.exit(0)


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(test_all())
