import unittest
import numpy as np
from lp_simplex_functions import simplex_minimize


class TestSimplexMinimize(unittest.TestCase):
    def test_basic_lp(self):
        # Minimize: x1 + 2x2
        # Subject to:
        #   -x1 + x2 <= 1
        #    x1 + 2x2 <= 4
        #   2x1 + x2 <= 6
        #   x1 >= 0, x2 >= 0
        c = [1, 2]
        A = [
            [-1, 1],
            [1, 2],
            [2, 1]
        ]
        b = [1, 4, 6]
        bounds = [(0, None), (0, None)]
        result = simplex_minimize(c, A, b, bounds)
        self.assertTrue(result.success)
        # result.x: optimal variable values (solution vector)
        # result.fun: minimum value of the objective function at the solution
        # result.message: solver status message
        self.assertAlmostEqual(result.x[0], 0, places=6)
        self.assertAlmostEqual(result.x[1], 0, places=6)
        self.assertAlmostEqual(result.fun, 0, places=6)

    def test_known_solution(self):
        # Second known-solution case: use a constraint that forces a non-zero optimum
        # Minimize: x1 + x2
        # Subject to: x1 + x2 >= 5  =>  -x1 - x2 <= -5
        # and x1, x2 >= 0
        c = [1, 1]
        A = [
            [-1, -1]
        ]
        b = [-5]
        bounds = [(0, None), (0, None)]
        result = simplex_minimize(c, A, b, bounds)
        self.assertTrue(result.success)
        # Objective must be 5 at optimum (sum of variables equals 5)
        self.assertAlmostEqual(result.fun, 5.0, places=6)

    def test_infeasible(self):
        # Infeasible example: x1 <= 1 and x1 >= 2
        c = [1, 0]
        A = [
            [1, 0],    # x1 <= 1
            [-1, 0]    # -x1 <= -2  => x1 >= 2
        ]
        b = [1, -2]
        bounds = [(None, None), (None, None)]
        result = simplex_minimize(c, A, b, bounds)
        # Expect solver to report infeasible (success False)
        self.assertFalse(result.success)
        # Message or status should reflect infeasibility
        self.assertTrue('infeasible' in result.message.lower() or result.status != 0)

    def test_unbounded(self):
        # Unbounded example: minimize -x1 with x1 >= 0 (no upper bound)
        c = [-1, 0]
        A = None
        b = None
        bounds = [(0, None), (0, None)]
        result = simplex_minimize(c, A, b, bounds)
        # Expect solver to indicate unbounded (success False)
        self.assertFalse(result.success)
        self.assertTrue('unbounded' in result.message.lower() or result.status != 0)

    def test_feasibility_of_solution(self):
        # Re-run a feasible example and verify A @ x <= b within tolerance
        c = [1, 2]
        A = [
            [-1, 1],
            [1, 2],
            [2, 1]
        ]
        b = [1, 4, 6]
        bounds = [(0, None), (0, None)]
        result = simplex_minimize(c, A, b, bounds)
        self.assertTrue(result.success)
        x = np.asarray(result.x)
        A_mat = np.asarray(A)
        b_vec = np.asarray(b)
        tol = 1e-8
        lhs = A_mat.dot(x)
        self.assertTrue(np.all(lhs <= b_vec + tol))


if __name__ == "__main__":
    unittest.main()