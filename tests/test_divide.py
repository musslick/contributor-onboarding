from src.utils import divide
import warnings
import pytest

def test_divide():
    a = 10
    b = 2

    assert divide(a, b) == 5.0

def test_divide_by_zero():
    a = 10
    b = 0
    
    with pytest.warns(UserWarning, match="Division by zero"):
        result = divide(a, b)
        assert result == float('inf')
