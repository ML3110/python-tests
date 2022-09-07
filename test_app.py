from app import Animal
import pytest


def test_getAge_equals():
    foo = Animal("Test", 19)
    assert foo.getAge() == 19


def test_setAge_gettingAgeReturnsAge():
    foo = Animal("Test", 4)
    foo.setAge(7)
    assert foo.getAge() == 7


def test_setAge_greaterThanZero():
    foo = Animal("Test", 1)
    foo.setAge(-1)
    assert foo.getAge() > 0


def test_setAge_negativeAgeValueReturnsFalse():
    foo = Animal("Test", 1)
    assert foo.setAge(-1) == False


def test_setAge_positiveAgeValueReturnsTrue():
    foo = Animal("Test", 2)
    assert foo.setAge(10) == True
