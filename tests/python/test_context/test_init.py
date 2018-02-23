# encoding: utf-8
from __future__ import absolute_import

import unittest
import logging

from logging_utils._compat import mock
from logging_utils.context import getLoggerWithContext, buildFormattedAndSortedContextStack
from logging_utils.context.adapter import LoggerAdapterWithContext


class GetLoggerWithContextTest(unittest.TestCase):

    def setUp(self):
        self.inner_logger = mock.MagicMock(spec=logging.Logger)
        self.inner_logger.info = mock.MagicMock()

        self.logger = getLoggerWithContext()
        self.logger.logger = self.inner_logger

    def test_getLoggerWithContext_returns_LoggerAdapterWithContext(self):
        self.assertIsInstance(getLoggerWithContext(), LoggerAdapterWithContext)

    def test_log_messages_contain_formatted_and_sorted_context_args(self):
        with self.logger.context(a=1):
            with self.logger.context(c=3):
                with self.logger.context(b=2):
                    self.logger.info("foo")
                    with self.logger.context(a=11):
                        self.logger.info("bar")
                self.logger.info("baz")

        self.inner_logger.info.assert_has_calls([
            mock.call("foo; [a]=[1]; [b]=[2]; [c]=[3]", extra=None),
            mock.call("bar; [a]=[11]; [b]=[2]; [c]=[3]", extra=None),
            mock.call("baz; [a]=[1]; [c]=[3]", extra=None)
        ])


class BuildFormattedAndSortedContextStackTest(unittest.TestCase):

    def setUp(self):
        self.stack = buildFormattedAndSortedContextStack()

    def test_log_messages_contain_formatted_and_sorted_context_args(self):
        self.stack.push(dict(a=1))
        self.stack.push(dict(c=3))
        self.stack.push(dict(b=2, d=4))
        self.stack.push(dict(d=14, a=11))

        self.assertEqual(str(self.stack), "[a]=[11]; [b]=[2]; [c]=[3]; [d]=[14]")

