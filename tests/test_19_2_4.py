import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 6, 4) == 10

    def test_multiply_success(self):
        assert  self.calc.multiply(self, 3, 5) == 15

    def test_division_success(self):
        assert self.calc.division(self, 20, 4) == 5

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 5, 10) == -5




