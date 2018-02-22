# encoding: utf-8
import unittest

AVAILABLE = True
try:
    from logging_utils.context.stack.chainmap import ContextStack
except:
    AVAILABLE = False


@unittest.skipUnless(AVAILABLE, "ChainMap-backed ContextStack is unavailable")
class ContextStackTest(unittest.TestCase):

    def setUp(self):
        self.stack = ContextStack()

    def test_pop_from_empty_stack_does_not_raise_IndexError(self):
        self.stack.pop()

    def test_push_does_not_care_about_value_types(self):
        self.stack.push(None)
        self.stack.push(1)
        self.stack.push([1,2,3])

    def test_to_str_complains_about_incorrect_value_type(self):
        self.stack.push(None)
        self.assertRaises(TypeError, str, self.stack)

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

