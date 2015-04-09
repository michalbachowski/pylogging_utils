# -*- coding: utf-8 -*-
"""
Python 2.7.x, 3.2+ compatability module.
"""
from __future__ import unicode_literals
import operator
import sys

is_py2 = sys.version_info[0] == 2

if not is_py2:
    # Python 3

    # lazy iterators
    map = map
    iteritems = operator.methodcaller(b'items')

    from unittest import mock
else:
    # Python 2

    # lazy iterators
    from itertools import imap
    map = imap
    iteritems = operator.methodcaller(b'iteritems')

    import mock

