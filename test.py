# test_fibonacci.py
from fibonacci import fibonacci  

def test_fibonacci_negative():
    result = fibonacci(-1)
    assert result == [], "fibonacci(-1) should return an empty list"

def test_fibonacci_zero():
    result = fibonacci(0)
    assert result == [], "fibonacci(0) should return an empty list"

def test_fibonacci_one():
    result = fibonacci(1)
    assert result == [0], "fibonacci(1) should return [0]"

def test_fibonacci_two():
    result = fibonacci(2)
    assert result == [0, 1], "fibonacci(2) should return [0, 1]"

def test_fibonacci_positive():
    result = fibonacci(10)
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert result == expected, "fibonacci(10) should return the first 10 Fibonacci numbers"

def test_fibonacci_invalid_input():
    result = fibonacci("invalid")
    assert result == [], "fibonacci('invalid') should return an empty list"

def test_fibonacci_large_input():
    result = fibonacci(100)
    assert len(result) == 100, "fibonacci(100) should return a list of 100 Fibonacci numbers"

if __name__ == "__main__":
    import pytest
    pytest.main()
