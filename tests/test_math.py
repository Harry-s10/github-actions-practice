from src.math_util import add, multiply, power


def test_add():
    assert add(1, 2) == 3


def test_multiply():
    assert multiply(2, 3) == 6


def test_power():
    assert power(2, 2) == 4
