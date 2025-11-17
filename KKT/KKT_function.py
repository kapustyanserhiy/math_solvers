import sympy as sp
def generate_kkt_conditions(objective, equalities=None, inequalities=None):

    # ======================================================
    # 1) Sympify objective and constraints and extract variables 
    # ======================================================
    detected_variables = set()

    # Objective
    objective_expr = sp.sympify(objective)
    detected_variables |= objective_expr.free_symbols

    # Equalities
    if equalities is None:
        equality_constraints = []
    else:
        equality_constraints = []
        for e in equalities:
            expr = sp.sympify(e)
            equality_constraints.append(expr)
            detected_variables |= expr.free_symbols

    # Inequalities
    if inequalities is None:
        inequality_constraints = []
    else:
        inequality_constraints = []
        for e in inequalities:
            expr = sp.sympify(e)
            inequality_constraints.append(expr)
            detected_variables |= expr.free_symbols

    # Sort variables 
    decision_variables = sorted(detected_variables, key=lambda v: v.name)


    # ======================================================
    # 2) Prepare dual variables
    # ======================================================
    num_equalities   = len(equality_constraints)
    num_inequalities = len(inequality_constraints)

    lagrange_multipliers   = sp.symbols(f"lambda_0:{num_equalities}")
    inequality_multipliers = sp.symbols(f"mu_0:{num_inequalities}")


    # ======================================================
    # 3) Build Lagrangian
    # ======================================================
    lagrangian = objective_expr

    for i in range(num_equalities):
        lagrangian += lagrange_multipliers[i] * equality_constraints[i]

    for j in range(num_inequalities):
        lagrangian += inequality_multipliers[j] * inequality_constraints[j]


    # ======================================================
    # 4) KKT Conditions
    # ======================================================
    # Stationarity
    stationarity_conditions = [
        sp.simplify(sp.diff(lagrangian, var))
        for var in decision_variables
    ]

    # Primal feasibility
    primal_equalities   = equality_constraints
    primal_inequalities = inequality_constraints

    # Dual feasibility
    dual_feasibility = inequality_multipliers

    # Complementary slackness
    complementary_slackness = [
        sp.simplify(inequality_multipliers[j] * inequality_constraints[j])
        for j in range(num_inequalities)
    ]


    # ======================================================
    # 5) OUTPUT
    # ======================================================
    print("\n================= KKT CONDITIONS =================\n")

    print("Detected decision variables:", decision_variables)

    print("\n1) Stationarity:")
    for var, eq in zip(decision_variables, stationarity_conditions):
        print(f"   ∂L/∂{var} = {eq} = 0")

    print("\n2) Primal Feasibility:")
    for eq in primal_equalities:
        print(f"   {eq} = 0")
    for ineq in primal_inequalities:
        print(f"   {ineq} ≤ 0")

    print("\n3) Dual Feasibility:")
    for mu in dual_feasibility:
        print(f"   {mu} ≥ 0")

    print("\n4) Complementary Slackness:")
    for cs in complementary_slackness:
        print(f"   {cs} = 0")

    print("\n===================================================\n")

