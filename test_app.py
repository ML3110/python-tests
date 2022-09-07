from app import Animal
import pytest


def test_getAge1():
    foo = Animal("Test", 19)
    assert foo.getAge() == 19


def test_setAge1():
    foo = Animal("Test", 4)
    foo.setAge(7)
    assert foo.getAge() == 7


def test_setAge2():
    foo = Animal("Test", 1)
    foo.setAge(-1)
    assert foo.getAge() > 0


def test_setAge3():
    foo = Animal("Test", 1)
    assert foo.setAge(-1) == False


def test_setAge4():
    foo = Animal("Test", 2)
    assert foo.setAge(10) == True
