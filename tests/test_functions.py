import pytest # type: ignore
from src.functions import Functions

class TestFunctions:

    def setup_method(self):
        self.func = Functions()

    def test_factorial_basic(self):
        assert self.func.factorial(0) == 1
        assert self.func.factorial(1) == 1
        assert self.func.factorial(5) == 120

    def test_factorial_larger_numbers(self):
        assert self.func.factorial(6) == 720
        assert self.func.factorial(10) == 3628800

    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            self.func.factorial(-1)

    def test_factorial_invalid_type(self):
        with pytest.raises(ValueError):
            self.func.factorial(3.14)

    def test_factorial_recursive_basic(self):
        assert self.func.factorial_recursive(0) == 1
        assert self.func.factorial_recursive(1) == 1
        assert self.func.factorial_recursive(5) == 120

    def test_factorial_recursive_large_numbers(self):
        assert self.func.factorial_recursive(6) == 720
        assert self.func.factorial_recursive(7) == 5040

    def test_factorial_recursive_negative(self):
        with pytest.raises(ValueError):
            self.func.factorial_recursive(-5)

    def test_fibo_basic(self):
        assert self.func.fibo(0) == 0
        assert self.func.fibo(1) == 1
        assert self.func.fibo(2) == 1
        assert self.func.fibo(3) == 2
        assert self.func.fibo(4) == 3
        assert self.func.fibo(5) == 5

    def test_fibo_sequence(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, expected_value in enumerate(expected):
            assert self.func.fibo(i) == expected_value

    def test_fibo_negative(self):
        with pytest.raises(ValueError):
            self.func.fibo(-1)

    def test_fibo_recursive_basic(self):
        assert self.func.fibo_recursive(0) == 0
        assert self.func.fibo_recursive(1) == 1
        assert self.func.fibo_recursive(2) == 1
        assert self.func.fibo_recursive(3) == 2
        assert self.func.fibo_recursive(4) == 3
        assert self.func.fibo_recursive(5) == 5

    def test_fibo_recursive_sequence(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, expected_value in enumerate(expected):
            assert self.func.fibo_recursive(i) == expected_value

    def test_fibo_recursive_negative(self):
        with pytest.raises(ValueError):
            self.func.fibo_recursive(-5)

    def test_factorial_equivalence(self):
        for n in range(0, 10):
            assert self.func.factorial(n) == self.func.factorial_recursive(n)

    def test_fibo_equivalence(self):
        for n in range(0, 15):
            assert self.func.fibo(n) == self.func.fibo_recursive(n)
