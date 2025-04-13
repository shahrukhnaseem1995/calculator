"""
Unit tests for calculator.py functions using pytest.
"""

import pytest
import calculator

def test_add():
    """Test the add() function with positive integers."""
    result = calculator.add(2, 3)
    assert result == 5

def test_subtract():
    """Test the subtract() function with positive integers."""
    result = calculator.subtract(5, 2)
    assert result == 3

def test_multiply():
    """Test the multiply() function with positive integers."""
    result = calculator.multiply(4, 3)
    assert result == 12

def test_divide():
    """Test the divide() function with non-zero divisor."""
    result = calculator.divide(10, 2)
    assert result == 5

def test_divide_by_zero():
    """Test that divide() raises ValueError when dividing by zero."""
    with pytest.raises(ValueError):
        calculator.divide(5, 0)
        