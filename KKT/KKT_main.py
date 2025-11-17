from KKT_function import generate_kkt_conditions


if __name__ == "__main__":
    # ==========================================================
    # Example
    # ==========================================================
    objective = "2*x1 + x2**2 + 3*x3"
    equalities = ["x1 + x2 - 3", "2*x1 - x2 - 1", "x3**3 - 1"]
    inequalities = ["x1 - 1", "-x2 + 2", "x3**2 - 4"]

    generate_kkt_conditions(
        objective=objective,
        equalities=equalities,
        inequalities=inequalities,
    )
