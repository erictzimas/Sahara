from Solver.Solver import Solver
import pytest

def test_finalCalculations():
    solver = Solver('2 / 5 * 3 + 4.3 - 2')
    assert(solver.finalCalculations() ==  3.5)
