# Math Solvers — Optimization Toolkit

## Overview
A comprehensive Python toolkit for optimization problems, including linear programming (LP) solvers, KKT condition generation, and visualization tools. This project demonstrates modern Python development practices with modular design, extensive documentation, and clear examples.

## Features

### 1. Linear Programming (LP) Simplex Solver
- **Location**: `simplex/`
- Wrapper around `scipy.optimize.linprog` with enhanced output
- Human-readable solution printing (x1=..., x2=..., objective=...)
- 2D feasibility region visualization with:
  - Constraint lines and shaded feasible region
  - Objective function contour lines
  - Optimal solution marker
  - Bounds visualization
- Example runner: `simplex/LP_simplex_main.py`
- Unit tests: `simplex/test_lp_simplex.py`

### 2. KKT Condition Generator
- **Location**: `KKT/`
- Symbolic KKT condition generation using SymPy
- Automatic variable detection from expressions
- Generates:
  - Stationarity conditions (∇L = 0)
  - Primal feasibility (equality and inequality constraints)
  - Dual feasibility (μ ≥ 0)
  - Complementary slackness (μᵢ·gᵢ = 0)
- Supports linear, quadratic, and nonlinear objective functions
- Example runner: `KKT/KKT_main.py`

## Project Structure
```
math_solvers/
├── KKT/                      # KKT condition utilities
│   ├── __init__.py
│   ├── KKT_function.py       # Symbolic KKT generator
│   └── KKT_main.py           # Example runner
├── simplex/                  # LP simplex solver
│   ├── lp_simplex_functions.py  # Solver and plotting
│   ├── LP_simplex_main.py       # Example runner
│   └── test_lp_simplex.py       # Unit tests
├── requirements.txt          # Python dependencies
├── Readme.txt                # This file
└── .gitignore                # Git ignore patterns
```

## Quick Start

### 1. Clone and Setup
```bash
git clone https://github.com/kapustyanserhiy/math_solvers.git
cd math_solvers

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Run LP Simplex Solver Example
```bash
python simplex/LP_simplex_main.py
```
This will solve a sample LP and display a 2D visualization.

### 3. Generate KKT Conditions
```bash
python KKT/KKT_main.py
```
Or from project root:
```bash
python -m KKT.KKT_main
```

### 4. Run Tests
```bash
python -m pytest simplex/test_lp_simplex.py
```

## Usage Examples

### LP Solver with Visualization
```python
from simplex.lp_simplex_functions import simplex_minimize, plot_simplex
import numpy as np

c = np.array([1.0, 2.0])
A_ub = np.array([[-1.0, 1.0], [1.0, 2.0], [2.0, 1.0]])
b_ub = np.array([1.0, 4.0, 6.0])
bounds = [(0, None), (0, None)]

result = simplex_minimize(c, A_ub, b_ub, bounds)
plot_simplex(c, A_ub, b_ub, bounds, result)
```

### Generate KKT Conditions
```python
from KKT.KKT_function import generate_kkt_conditions

objective = "2*x1 + x2**2 + 3*x3"
equalities = ["x1 + x2 - 3", "2*x1 - x2 - 1"]
inequalities = ["x1 - 1", "-x2 + 2"]

generate_kkt_conditions(
    objective=objective,
    equalities=equalities,
    inequalities=inequalities
)
```

## Dependencies
- **numpy** — Array operations and linear algebra
- **scipy** — Optimization algorithms (linprog)
- **matplotlib** — Plotting and visualization
- **sympy** — Symbolic mathematics for KKT generation

See `requirements.txt` for version details.

## Development

### Code Style
- Follow PEP 8 conventions
- Use type hints where appropriate
- Document functions with docstrings
- Keep functions focused and testable

### Testing
Unit tests are located in the module directories:
- `simplex/test_lp_simplex.py` — LP solver tests

Run all tests:
```bash
python -m pytest
```

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Submit a pull request

## License
Open source. Free to use and modify.

## Author
Serhiy Kapustyan  
GitHub: [@kapustyanserhiy](https://github.com/kapustyanserhiy)

## Repository
https://github.com/kapustyanserhiy/math_solvers
