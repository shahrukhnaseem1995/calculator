import pytest
import calculator

def test_add():
    result = calculator.add(2, 3)
    assert result == 5

def test_subtract():
    result = calculator.subtract(5, 2)
    assert result == 3

def test_multiply():
    result = calculator.multiply(4, 3)
    assert result == 12

def test_divide():
    result = calculator.divide(10, 2)
    assert result == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(5, 0)

