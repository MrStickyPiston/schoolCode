import os

import sympy

# DONT REMOVE THIS IS USED IN EVAL()
from math import exp, log, sqrt


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def frequency(f=sympy.symbols("f"), t=sympy.symbols("t")):
    equation = sympy.Eq(1 / t, f)
    solution = sympy.solve(equation)
    return eval(str(solution[0]))


def speed(s=sympy.symbols("s"), v=sympy.symbols("v"), t=sympy.symbols("t")):
    equation = sympy.Eq(v * t, s)
    solution = sympy.solve(equation)
    return eval(str(solution[0]))


def length(l=sympy.symbols("l"), v=sympy.symbols("v"), f=sympy.symbols("f")):
    equation = sympy.Eq(v / f, l)
    solution = sympy.solve(equation)
    return eval(str(solution[0]))


def decibels(i=sympy.symbols("i"), db=sympy.symbols("d")):
    equation = sympy.Eq(10 * sympy.log(i / 1e-12, 10), db)
    solution = sympy.solve(equation)
    return eval(str(solution[0]))


def decibel_difference(dL=sympy.symbols('dL'),
                       R1=sympy.symbols('R1'),
                       R2=sympy.symbols('R2')):
    """Based on https://www.engineeringtoolbox.com/inverse-square-law-d_890.html
Calculates the difference of decibel by distance to the source

dL: decibel difference\n
R1: the first positions meters to the source\n
R2: the second positions meters to the source\n"""
    equation = sympy.Eq(20 * sympy.log(R1 / R2, 10), dL)
    solution = sympy.solve(equation)
    return eval(str(solution[0]))


if __name__ == '__main__':
    formulas = [("frequency             ", "f=1/t                   ", "Calculate frequency or vibration time"),
                ("speed                 ", "s=v*t                   ", "Calculate the speed, speed or time"),
                ("length                ", "l=v/f                   ", "Calculate the wave length, speed or frequency"),
                ("decibels              ", "db = 10log10(i / 1e-12) ", "Calculate the decibels or the sound intensity"),
                ("decibel_difference    ", "dL = 20log10(R1 / R2)   ",
                 "Calculate the difference in meter or the amount of decibel")]
    menu = "".join([f"[{formulas.index(i)}] {i[0]}  {i[1]}  {i[2]}\n" for i in formulas])

    while True:
        clear()
        formula = input(f"ID  Name                    Formula                   Description\n{menu}\nFormula: ")
        try:
            if formula.isnumeric():
                formula = formulas[int(formula)][0]
        except IndexError as e:
            print(e)
        try:
            input(
                f"Formula output: {eval(f'''{formula}({input('Enter formula args: ')})''')}\n\nPress enter to continue...")
        except SyntaxError as e:
            print(f"Error: {e.msg}\n")
