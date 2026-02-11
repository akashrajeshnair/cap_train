import pytest 

def func(x):
    return x + 5

def test_method():
    assert func(3) == 8

pytest.main(['test_sample.py'])