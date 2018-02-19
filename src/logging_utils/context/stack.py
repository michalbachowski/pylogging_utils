# -*- coding: utf-8 -*-
""" Module contains implementation for context stack """
from __future__ import absolute_import

from itertools import chain
from collections import OrderedDict
from .._compat import iteritems, map

class ContextStack(object):

    def __init__(self):
        self._stack = []
        self._dict_cache = OrderedDict()
        self._str_cache = None
        self._format_context_arg = lambda tpl: "{0}={1}".format(tpl[0], tpl[1])

    def push(self, context):
        self._dict_cache.update(context)
        self._stack.append(context)
        self._str_cache = None
        return self

    def pop(self):
        self._stack.pop()
        self._dict_cache = dict(chain.from_iterable(map(iteritems, self._stack)))
        self._str_cache = None
        return self

    def __str__(self):
        if self._str_cache is None:
            self._str_cache = '; '.join(map(self._format_context_arg,
                                            iteritems(self._dict_cache)))
        return self._str_cache

