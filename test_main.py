import pytest
from main import factorial

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_small():
    assert factorial(5) == 120

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)
