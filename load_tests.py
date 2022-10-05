#!/usr/bin/env python
#import os, sys
import sys
from unittest import TestSuite

from boot_django import boot_django

# call the django setup routine
boot_django()

tests = [
    "magicadmin.tests.test_models",
    "magicadmin.tests.test_views",
]

def get_suite(labels=tests):
    from django.test.runner import DiscoverRunner
    runner = DiscoverRunner(verbosity=1)
    import ipdb; ipdb.set_trace()
    failures = runner.run_tests(labels)
    if failures:
        sys.exit(failures)

    # in case this is called from setup tools, return a test suite
    return TestSuite()


if __name__ == "__main__":
    get_suite()