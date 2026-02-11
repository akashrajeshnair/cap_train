import pytest

def test_answer1():
    a, b = 5, 10
    assert a == b

def test_answer2():
    c = 15
    d = 3*5
    assert c == d

pytest.main(['multiple.py'])