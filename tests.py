import math
from calculator import Calculator
import pandas as pd
from math import sqrt
from colorama import Back, Fore, Style

def compareFloats(a, b):
    return round(a, 2) == round(b, 2)



def dataFromCsv(filename:str):
    df = pd.read_csv(filename)
    values = df.values.tolist()
    return values



def TestAddition(calc:Calculator):
    print(Fore.BLACK + Back.YELLOW + "Test for addition" + Style.RESET_ALL)
    values = dataFromCsv("./test-data/UnitTestAddition.csv")
    total = len(values)
    passed = 0
    failed = 0
    for row in values:
        print(f'{row[0]} + {row[1]} = ', end="")
        res = calc.Addition(row[0], row[1])
        print(res, end=" ")

        if res != row[2]:
            print(Fore.RED + "Test Failed ❌" + Style.RESET_ALL)
            failed += 1

        else:
            print(Fore.GREEN + "Test Passed 💚" + Style.RESET_ALL)
            passed += 1
    
    print(f'Total tests = {total}\nPassed = {passed}\nFailed = {failed}')


def TestSubtraction(calc:Calculator):
    print(Fore.BLACK + Back.YELLOW + "Test for subtraction" + Style.RESET_ALL)
    values = dataFromCsv("./test-data/UnitTestSubtraction.csv")
    total = len(values)
    passed = 0
    failed = 0
    for row in values:
        print(f'{row[0]} - {row[1]} = ', end="")
        row[2] = row[0]- row[1]
        res = calc.Subtraction(row[0], row[1])
        print(res, end=" ")

        if res != row[2]:
            print(Fore.RED + "Test Failed ❌" + Style.RESET_ALL)
            failed += 1

        else:
            print(Fore.GREEN + "Test Passed 💚" + Style.RESET_ALL)
            passed += 1

        
        
        
    print(f'Total tests = {total}\nPassed = {passed}\nFailed = {failed}')


def TestMultiplication(calc:Calculator):
    print(Fore.BLACK + Back.YELLOW + "Test for Multiplication" + Style.RESET_ALL)
    values = dataFromCsv("./test-data/UnitTestMultiplication.csv")
    total = len(values)
    passed = 0
    failed = 0
    for row in values:
        print(f'{row[0]} * {row[1]} = ', end="")
        res = calc.Multiplication(row[0], row[1])
        print(res, end=" ")

        if res != row[2]:
            print(Fore.RED + "Test Failed ❌" + Style.RESET_ALL)
            failed += 1

        else:
            print(Fore.GREEN + "Test Passed 💚" + Style.RESET_ALL)
            passed += 1


    print(f'Total tests = {total}\nPassed = {passed}\nFailed = {failed}')



def TestDivision(calc:Calculator):
    print(Fore.BLACK + Back.YELLOW + "Test for Division" + Style.RESET_ALL)
    values = dataFromCsv("./test-data/UnitTestDivision.csv")
    total = len(values)
    passed = 0
    failed = 0
    for row in values:
        print(f'{row[0]} / {row[1]} = ', end="")
        res = calc.Division(row[0], row[1])
        print(res, end=" ")

        if not compareFloats(res, row[2]):
            print(Fore.RED + "Test Failed ❌" + Style.RESET_ALL)
            failed += 1

        else:
            print(Fore.GREEN + "Test Passed 💚" + Style.RESET_ALL)
            passed += 1

        print(res)
    print(f'Total tests = {total}\nPassed = {passed}\nFailed = {failed}')




def TestSquare(calc:Calculator):
    print(Fore.BLACK + Back.YELLOW + "Test for Square" + Style.RESET_ALL)
    values = dataFromCsv("./test-data/UnitTestSquare.csv")
    total = len(values)
    passed = 0
    failed = 0
    for row in values:
        print(f'Square of {row[0]} = ', end="")
        res = calc.Square(row[0])
        print(res, end=" ")

        if row[1] != res:
            print(Fore.RED + "Test Failed ❌" + Style.RESET_ALL)
            failed += 1

        else:
            print(Fore.GREEN + "Test Passed 💚" + Style.RESET_ALL)
            passed += 1
        

    
    print(f'Total tests = {total}\nPassed = {passed}\nFailed = {failed}')





def TestSquareRoot(calc:Calculator):
    print(Fore.BLACK + Back.YELLOW + "Test for Square Root" + Style.RESET_ALL)
    values = dataFromCsv("./test-data/UnitTestSquareRoot.csv")
    total = len(values)
    passed = 0
    failed = 0
    for row in values:
        print(f'Square Root of {row[0]} = ', end="")
        res = calc.SquareRoot(row[0])
        print(res, end=" ")

        if not compareFloats(res, row[1]):
            print(Fore.RED + "Test Failed ❌" + Style.RESET_ALL)
            failed += 1

        else:
            print(Fore.GREEN + "Test Passed 💚" + Style.RESET_ALL)
            passed += 1
        

    
    print(f'Total tests = {total}\nPassed = {passed}\nFailed = {failed}')



