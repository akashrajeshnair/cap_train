import pytest

def prime(n):
    f = []
    for i in range(1, (n//2)+1):
        if n%i == 0:
            f.append(i)
    f.append(n)
    if sum(f) == n+1:
        return True
    return False

def test_method():
    assert prime(23) == True

pytest.main(['prime.py'])