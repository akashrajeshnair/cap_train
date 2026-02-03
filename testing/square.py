import pytest

def square(n):
    return n*n

def test_method():
    assert square(2) == 4

pytest.main(['square.py'])