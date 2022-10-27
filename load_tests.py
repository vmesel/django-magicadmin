#!/usr/bin/env python
#import os, sys
import sys
from unittest import TestSuite

from boot_django import boot_django

# call the django setup routine
boot_django()

tests = [
    "django_magicadmin.tests.test_models",
    "django_magicadmin.tests.test_views",
]

def get_suite(labels=tests):
    from django.test.runner import DiscoverRunner
    runner = DiscoverRunner(verbosity=1)
    failures = runner.run_tests(labels)
    if failures:
        sys.exit(failures)

    # in case this is called from setup tools, return a test suite
    return TestSuite()


if __name__ == "__main__":
    get_suite()
