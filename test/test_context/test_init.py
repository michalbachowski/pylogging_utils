# encoding: utf-8
from __future__ import absolute_import

import unittest
import logging
from collections import OrderedDict

from logging_utils._compat import mock
from logging_utils.context.stack import ContextStack

from logging_utils.context import LoggerContextual

class IsA(object):
    """Comparator class that checks if given object is instance of given type"""

    def __init__(self, cls):
        """ Obect initialization """
        self.cls = cls

    def __eq__(self, other):
        """ Equality check"""
        return isinstance(other, self.cls)

class LoggerContextualTest(unittest.TestCase):

    def setUp(self):
        self.real_logger = mock.MagicMock(spec=logging.Logger)
        self.stack = mock.MagicMock(spec=ContextStack)
        self.stack.__str__.return_value = 'stack_return'
        self.logger = LoggerContextual(self.stack, self.real_logger)

    def test_process_returns_message_with_appended_context_stack(self):
            self.assertEqual('message; stack_return',
                             self.logger.process('message', {})[0])

    def test_logger_uses_context_management_to_manage_stack(self):
        self.assertEqual(0, self.stack.push.call_count)
        self.assertEqual(0, self.stack.pop.call_count)

        with self.logger.context(foo=1):
            self.stack.push.assert_called_once_with(IsA(OrderedDict))
            self.assertEqual(0, self.stack.pop.call_count)

            self.assertEqual('message; stack_return',
                             self.logger.process('message', {})[0])

        self.stack.push.assert_called_once_with(IsA(OrderedDict))
        self.stack.pop.assert_called_once_with()

