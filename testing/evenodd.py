import pytest 

def even(n):
    return n%2 == 0

def test_method():
    assert even(2) is True

pytest.main(['evenodd.py'])