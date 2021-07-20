from Solver.Solver import Solver
import pytest


def test_finalCalculations():
    solver = Solver("2 / 5 * 3 + 4.3 - 2")
    assert solver.finalCalculations() == 3.5


def test_floatEquation():
    solver = Solver("2 + 5 - 2 / 4")
    result = [2.0, "+", 5.0, "-", 2.0, "/", 4.0]
    assert solver.floatEquation() == result


def test_parenthesis():
    solver = Solver("( 2 - 5 ) * 2")
    assert solver.parenthesis() == -6.0


def test_firstDegreeCalculations():
    solver = Solver("x + 5 - 2 / 2")
    assert solver.firstDegreeCalculations() == -4.0


def test_secondDegreeCalculations():
    solver = Solver("d - 9")
    assert solver.secondDegreeCalculations() == "X1 = 3.0 X2 = -3.0"
