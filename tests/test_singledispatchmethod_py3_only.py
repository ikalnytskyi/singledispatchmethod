"""Test py3-only features of @singledispatchmethod decorator."""

import sys
import unittest

import pytest

from singledispatchmethod import singledispatchmethod


class TestSingleDispatchMethod(unittest.TestCase):
    """Backported tests from CPython source tree."""

    @pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python3.7+")
    def test_type_ann_register(self):
        class A(object):
            @singledispatchmethod
            def t(self, arg):
                return "base"

            @t.register
            def _(self, arg: int):
                return "int"

            @t.register
            def _(self, arg: str):
                return "str"

        a = A()

        self.assertEqual(a.t(0), "int")
        self.assertEqual(a.t(""), "str")
        self.assertEqual(a.t(0.0), "base")
