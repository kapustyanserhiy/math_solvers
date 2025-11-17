import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


def plot_simplex(c, A, b, bounds, result=None):

    
    plt.rcParams.update({'font.family': 'Arial', 'font.size': 16})

    x1s = np.linspace(-1, 10, 400)
    x2s = np.linspace(-1, 10, 400)
    X1, X2 = np.meshgrid(x1s, x2s)
    feasible = np.ones_like(X1, dtype=bool)
    
    for i in range(len(A)):
        feasible &= (A[i][0]*X1 + A[i][1]*X2 <= b[i])
    # Apply bounds
    if bounds[0][0] is not None:
        feasible &= (X1 >= bounds[0][0])
    if bounds[0][1] is not None:
        feasible &= (X1 <= bounds[0][1])
    if bounds[1][0] is not None:
        feasible &= (X2 >= bounds[1][0])
    if bounds[1][1] is not None:
        feasible &= (X2 <= bounds[1][1])

    plt.figure(figsize=(6,6))
    plt.contourf(X1, X2, feasible, levels=[0.5, 1], colors=['#d0f0d0'])
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Feasible region and optimal solution')

    # Plot bounds as dashed lines (after figure creation)
    if bounds[0][0] is not None:
        plt.axvline(bounds[0][0], color='grey', linestyle='--', label='x1 bound')
    if bounds[0][1] is not None:
        plt.axvline(bounds[0][1], color='grey', linestyle='--', label='x1 bound')
    if bounds[1][0] is not None:
        plt.axhline(bounds[1][0], color='grey', linestyle='--', label='x2 bound')
    if bounds[1][1] is not None:
        plt.axhline(bounds[1][1], color='grey', linestyle='--', label='x2 bound')

    # Plot constraint lines
    for i in range(len(A)):
        if A[i][1] != 0:
            x2_line = (b[i] - A[i][0]*x1s) / A[i][1]
            plt.plot(x1s, x2_line, label=f'Constraint {i+1}')
        else:
            x1_val = b[i]/A[i][0] if A[i][0] != 0 else 0
            plt.axvline(x1_val, label=f'Constraint {i+1}')

    # Plot objective function contour lines
    Z = c[0]*X1 + c[1]*X2
    contours = plt.contour(X1, X2, Z, levels=10, colors='blue', alpha=0.4, linewidths=1)
    plt.clabel(contours, inline=True, fontsize=8)

    # Plot the solution
    if result is not None and hasattr(result, 'x') and result.success:
        plt.plot(result.x[0], result.x[1], 'ro', markersize=10, label='Optimal solution')

    plt.xlim(x1s[0], x1s[-1])
    plt.ylim(x2s[0], x2s[-1])
    plt.legend()
    plt.grid(True, linestyle=':')
    plt.show()



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
        if len(result.x) >= 2:
            print(f"Optimal solution: [x1={result.x[0]}, x2={result.x[1]}]")
        else:
            print("Optimal solution:", result.x)
        print("Objective value at that point(y):", result.fun)
    else:
        print("Optimization failed:", result.message)
    
    return result

