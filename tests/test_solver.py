from Solver.Solver import Solver
import pytest

def test_finalCalculations():
    solver = Solver('3 + 3')
    assert(solver.finalCalculations() ==  6.0)
