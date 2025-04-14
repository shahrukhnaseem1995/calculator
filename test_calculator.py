"""
Unit tests for calculator.py functions using pytest, with logging.
"""

import os
from datetime import datetime
import pytest
import calculator

# Define the log path
LOG_DIR = "test-logs"
LOG_FILE = os.path.join(LOG_DIR, "test_run_log.txt")

# Ensure the log directory exists
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

def log_test(test_name):
    """Helper to write a log entry for a test."""
    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.now()}] Ran {test_name}\n")

def test_add():
    log_test("test_add")
    result = calculator.add(2, 3)
    assert result == 5

def test_subtract():
    log_test("test_subtract")
    result = calculator.subtract(5, 2)
    assert result == 3

def test_multiply():
    log_test("test_multiply")
    result = calculator.multiply(4, 3)
    assert result == 12

def test_divide():
    log_test("test_divide")
    result = calculator.divide(10, 2)
    assert result == 5

def test_divide_by_zero():
    log_test("test_divide_by_zero")
    with pytest.raises(ValueError):
        calculator.divide(5, 0)
