from calculator import Calculator
from tests import TestAddition, TestMultiplication, TestSubtraction

calc = Calculator()

TestAddition(calc)
TestSubtraction(calc)
TestMultiplication(calc)