from calculator import Calculator
from tests import TestAddition, TestDivision, TestMultiplication, TestSquare, TestSquareRoot, TestSubtraction

calc = Calculator()

TestAddition(calc)
TestSubtraction(calc)
TestMultiplication(calc)
TestDivision(calc)
TestSquare(calc)
TestSquareRoot(calc)
