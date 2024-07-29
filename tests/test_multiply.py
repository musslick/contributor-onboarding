from utils import multiply, divide
# import pytest

def test_multiply():
    a = 2
    b = 3

    assert multiply(a, b) == 6


def test_divide_positive_numbers():
    assert divide(10.0, 2.0) == 5.0


def test_divide_negative_numbers():
    assert divide(-10.0, -2.0) == 5.0


def test_divide_positive_and_negative():
    assert divide(10.0, -2.0) == -5.0


def test_divide_by_one():
    assert divide(10.0, 1.0) == 10.0


def test_divide_by_fraction():
    assert divide(10.0, 0.5) == 20.0


def test_divide_zero():
    assert divide(0.0, 10.0) == 0.0
    print("Test passed")


# def test_divide_by_zero():
#     with pytest.raises(ZeroDivisionError):
#         divide(10.0, 0.0)
