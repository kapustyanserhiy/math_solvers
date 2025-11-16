import unittest
from lp_simplex import simplex_minimize

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
        # Print actual result for debugging
        print('Solver result:', result)
        print('x:', result.x)
        print('fun:', result.fun)
        print('success:', result.success)
        print('message:', result.message)
        # Actual solution for this problem: x1=0, x2=0 (minimum value 0)
        self.assertAlmostEqual(result.x[0], 0, places=4)
        self.assertAlmostEqual(result.x[1], 0, places=4)
        self.assertAlmostEqual(result.fun, 0, places=4)

if __name__ == "__main__":
    unittest.main()
