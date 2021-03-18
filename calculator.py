from math import sqrt

class Calculator():
    def __init__(self):
        self.lastCalculation = 0

    def Addition(self, a:int, b:int):
        if type(a) != int or type(b) != int:
            raise ValueError("Entered values are not of int type")

        else:
            self.lastCalculation = a+b
            return self.lastCalculation

    def Subtraction(self, a:int, b:int):
        if type(a) != int or type(b) != int:
            raise ValueError("Entered values are not of int type")

        else:
            self.lastCalculation = a-b
            return self.lastCalculation

    def Multiplication(self, a:int, b:int):
        if type(a) != int or type(b) != int:
            raise ValueError("Entered values are not of int type")

        else:
            self.lastCalculation = a*b
            return self.lastCalculation


    def Division(self, a:int, b:int):

        if b==0:
            raise ValueError("Division cannot be performed on denominator 0")

        else:
            self.lastCalculation = b/a
            return self.lastCalculation


    def Square(self, n:int):
        self.lastCalculation = n**2
        return self.lastCalculation



    def SquareRoot(self, n:int):
        self.lastCalculation = sqrt(n)
        return self.lastCalculation
    

    

    
