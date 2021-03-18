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



