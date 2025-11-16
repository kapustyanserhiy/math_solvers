from scipy.optimize import linprog


def simplex_minimize(c, A, b, bounds=None):
    """
    Solve a linear programming problem using the simplex-like 'highs-ds' method.

    Minimize:      cᵀ x
    Subject to:    A_ub x ≤ b_ub
                   bounds[i] = (lower_i, upper_i) for each variable
    """
    return linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs-ds")



if __name__ == "__main__":


    # -------------------------------------------------------------
    # OBJECTIVE FUNCTION
    # Minimize: 1*x1 + 2*x2
    # c = [coeff_x1, coeff_x2]
    # -------------------------------------------------------------
    c = [1, 2]


    # -------------------------------------------------------------
    # INEQUALITY CONSTRAINT MATRIX (A) and RHS vector (b)
    #
    # Each row of A represents one constraint of the form:
    #   a11*x1 + a12*x2 ≤ b_i
    #
    # Example constraints:
    #   -x1 +  x2 ≤ 1   →  [-1, 1], 1
    #    x1 + 2x2 ≤ 4   →  [ 1, 2], 4
    #   2x1 +  x2 ≤ 6   →  [ 2, 1], 6
    #
    # If you want to add or change constraints, update both A and b accordingly.
    # -------------------------------------------------------------
    A = [
        [-1,  1],   # -x1 + x2 ≤ 1
        [ 1,  2],   #  x1 + 2x2 ≤ 4
        [ 2,  1]    #  2x1 + x2 ≤ 6
    ]

    b = [1, 4, 6]   # right-hand side values for each constraint


  

    # -------------------------------------------------------------
    # VARIABLE BOUNDS
    # bounds = [(lower_x1, upper_x1), (lower_x2, upper_x2), ...]
    # None means no bound in that direction (unbounded)
    # -------------------------------------------------------------
    bounds = [(0, None),    # x1 ≥ 0
              (0, None)]   # x2 ≥ 0



    # -------------------------------------------------------------
    # SOLVE LP
    # -------------------------------------------------------------
    result = simplex_minimize(c, A, b, bounds=bounds)


    # -------------------------------------------------------------
    # OUTPUT RESULTS
    # -------------------------------------------------------------
    if result.success:
        print("Optimal solution (x):", result.x)
        print("Minimum objective value:", result.fun)
    else:
        print("Optimization failed:", result.message)
        print("Full SciPy result object:", result)
