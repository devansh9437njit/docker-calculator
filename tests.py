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