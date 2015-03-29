#!/usr/bin/env python
# encoding: utf-8

import os
import sys


os.environ["DJANGO_SETTINGS_MODULE"] = "testapp.tests.settings"


def main():
    import django
    django.setup()

    from django.conf import settings
    from django.test.utils import get_runner

    TestRunner = get_runner(settings)

    test_runner = TestRunner()
    failures = test_runner.run_tests(['testapp'])

    sys.exit(failures)


if __name__ == '__main__':
    main()
