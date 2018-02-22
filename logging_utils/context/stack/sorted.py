# -*- coding: utf-8 -*-

from operator import itemgetter

class SortedContextStack(object):

    def __init__(self, inner):
        self._stack = inner

    def push(self, context):
        self._stack.push(context)
        return self

    def pop(self):
        self._stack.pop()
        return self

    def get_items(self):
        return sorted(self._stack.get_items(), key=itemgetter(0))

    def __str__(self):
        return str(self._stack)

