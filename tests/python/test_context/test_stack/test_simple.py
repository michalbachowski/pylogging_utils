# encoding: utf-8
import unittest

from logging_utils.context.stack.simple import ContextStack


class ContextStackTest(unittest.TestCase):

    def setUp(self):
        self.stack = ContextStack()

    def test_pop_from_empty_stack_raises_IndexError(self):
        self.assertRaises(IndexError, self.stack.pop)

    def test_push_expects_value_to_be_dict(self):
        self.assertRaises(TypeError, self.stack.push, None)
        self.assertRaises(TypeError, self.stack.push, 1)
        self.assertRaises(TypeError, self.stack.push, [1,2,3])

    def test_stack_might_be_casted_to_string(self):
        self.assertEqual('', str(self.stack))

        self.stack.push({'a': 1})
        self.assertEqual('a=1', str(self.stack))

        self.stack.push({'b': 2})
        self.assertEqual('a=1; b=2', str(self.stack))

        self.stack.pop()
        self.assertEqual('a=1', str(self.stack))

        self.stack.pop()
        self.assertEqual('', str(self.stack))

    def test_new_context_overrides_existing_values(self):

        self.stack.push({'a': 1})
        self.assertEqual('a=1', str(self.stack))

        self.stack.push({'a': 2})
        self.assertEqual('a=2', str(self.stack))

        self.stack.pop()
        self.assertEqual('a=1', str(self.stack))

