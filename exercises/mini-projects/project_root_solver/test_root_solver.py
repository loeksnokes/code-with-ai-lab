import math
import pytest
from project_root_solver.root_solver import newton_method

def test_newton_method_sqrt2_converges():
    f = lambda x: x * x - 2
    df = lambda x: 2 * x

    root = newton_method(f, df, x0=1.0)

    assert root == pytest.approx(math.sqrt(2), rel=1e-7)
    assert f(root) == pytest.approx(0.0, abs=1e-7)