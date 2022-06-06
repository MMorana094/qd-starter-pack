#
#  Write a program that given two numbers as input make the main operations.
#  Output:
#  Insert first number: 4
#  Insert second number: 2
#  SUM: 6
#  Difference: 2
#  Multiplication: 8
# Division

from typing import Union
def sum(a: Union[int, float], b: Union[int, float]) :
    return a + b

def diff(a: Union[int, float], b: Union[int, float]) :
    return a - b

def mult(a: Union[int, float], b: Union[int, float]) :
    return a * b
