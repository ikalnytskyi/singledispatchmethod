"""Test @singledispatchmethod decorator."""

import abc
import unittest

import pytest

from singledispatchmethod import singledispatchmethod


class TestSingleDispatchMethod(unittest.TestCase):
    """Backported tests from CPython source tree."""

    def test_method_register(self):
        class A(object):
            @singledispatchmethod
            def t(self, arg):
                self.arg = "base"

            @t.register(int)
            def _(self, arg):
                self.arg = "int"

            @t.register(str)
            def _(self, arg):
                self.arg = "str"

        a = A()

        a.t(0)
        self.assertEqual(a.arg, "int")
        aa = A()
        self.assertFalse(hasattr(aa, "arg"))
        a.t("")
        self.assertEqual(a.arg, "str")
        aa = A()
        self.assertFalse(hasattr(aa, "arg"))
        a.t(0.0)
        self.assertEqual(a.arg, "base")
        aa = A()
        self.assertFalse(hasattr(aa, "arg"))

    def test_staticmethod_register(self):
        class A(object):
            @singledispatchmethod
            @staticmethod
            def t(arg):
                return arg

            @t.register(int)
            @staticmethod
            def _(arg):
                return isinstance(arg, int)

            @t.register(str)
            @staticmethod
            def _(arg):
                return isinstance(arg, str)

        self.assertTrue(A.t(0))
        self.assertTrue(A.t(""))
        self.assertEqual(A.t(0.0), 0.0)

    def test_classmethod_register(self):
        class A(object):
            def __init__(self, arg):
                self.arg = arg

            @singledispatchmethod
            @classmethod
            def t(cls, arg):
                return cls("base")

            @t.register(int)
            @classmethod
            def _(cls, arg):
                return cls("int")

            @t.register(str)
            @classmethod
            def _(cls, arg):
                return cls("str")

        self.assertEqual(A.t(0).arg, "int")
        self.assertEqual(A.t("").arg, "str")
        self.assertEqual(A.t(0.0).arg, "base")

    def test_callable_register(self):
        class A(object):
            def __init__(self, arg):
                self.arg = arg

            @singledispatchmethod
            @classmethod
            def t(cls, arg):
                return cls("base")

        @A.t.register(int)
        @classmethod
        def _(cls, arg):
            return cls("int")

        @A.t.register(str)
        @classmethod
        def _(cls, arg):
            return cls("str")

        self.assertEqual(A.t(0).arg, "int")
        self.assertEqual(A.t("").arg, "str")
        self.assertEqual(A.t(0.0).arg, "base")

    def test_abstractmethod_register(self):
        class Abstract(abc.ABCMeta):
            @singledispatchmethod
            @abc.abstractmethod
            def add(self, x, y):
                pass

        self.assertTrue(Abstract.add.__isabstractmethod__)


def test_type_not_callable_not_descriptor():
    with pytest.raises(TypeError) as excinfo:
        singledispatchmethod(42)
    assert str(excinfo.value) == "42 is not callable or a descriptor"

    with pytest.raises(TypeError) as excinfo:
        singledispatchmethod(True)
    assert str(excinfo.value) == "True is not callable or a descriptor"
