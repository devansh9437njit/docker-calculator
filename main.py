from calculator import Calculator
from tests import TestAddition, TestDivision, TestMultiplication, TestSubtraction

calc = Calculator()

TestAddition(calc)
TestSubtraction(calc)
TestMultiplication(calc)
TestDivision(calc)
