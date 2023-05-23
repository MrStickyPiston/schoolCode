import sympy
from sympy import I
from math import *


def evaluate_solution(solution: list = "None") -> list:
    """Evaluates mathematical solutions
    :param solution: array of unevaluated solutions
    :return: list of evaluated solutions"""

    out = []
    for i in solution:
        out.append(eval(str(i)))
    return out


def quadratic(a: float = sympy.symbols("a"),
              b: float = sympy.symbols("b"),
              c: float = sympy.symbols("c"),
              x: float = sympy.symbols("x"),
              y: float = 0) -> list:

    """Solves a quadratic equation in the form of y=ax^2+bx+c
    :param a: quadratic value of the equation
    :param b: linear value of the equation
    :param c: The
    :param x: x of the quadratic equation
    :param y: y value of the quadratic equation
    :return: list of all possible solutions"""

    equation = sympy.Eq((a * x ** 2) + b * x + c, y)
    solution = sympy.solve(equation)
    return evaluate_solution(solution)


solution = eval(f"quadratic({input('Enter variables: ')})")
print(" V ".join(str(i) for i in solution))
