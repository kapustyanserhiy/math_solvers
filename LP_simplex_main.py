
import lp_simplex_functions

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
     bounds = [
          (0, None),    # x1 ≥ 0
          (0, None)     # x2 ≥ 0
     ]

     # Run the solver
     result = lp_simplex_functions.simplex_minimize(c, A, b, bounds=bounds)

     # Plot the feasible region and solution (only for 2 variables)
     lp_simplex_functions.plot_simplex(c, A, b, bounds, result)


