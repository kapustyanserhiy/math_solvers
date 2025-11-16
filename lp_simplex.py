from scipy.optimize import linprog


def simplex_minimize(c, A, b, bounds=None):
    """
    Solve a linear programming problem using the simplex-like 'highs-ds' method.

    Minimize:      cᵀ x
    Subject to:    A_ub x ≤ b_ub
                   bounds[i] = (lower_i, upper_i) for each variable
    """
    
    # -------------------------------------------------------------
    # OUTPUT RESULTS
    # -------------------------------------------------------------
    result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs-ds")
    
    if result.success:
        print("Optimal solution (x):", result.x)
        print("Minimum objective value:", result.fun)
    else:
        print("Optimization failed:", result.message)
    
    return result





      
