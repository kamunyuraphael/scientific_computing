# BIT 2118 – Scientific Computing: Individual Repository

**Student:** Kamunyu Raphael · **Reg. no:** BSCCS/2024/45844 · **Unit:** BIT 2118 Scientific Computing

Each task (2 to 20) has a program, console output, documentation and, where useful, a figure. The documentation for every task follows the brief:

| Brief item | Where it is in each `docs/Task_XX_*.md` |
|---|---|
| B. Identify input values and the mathematical operation | Section **B** |
| C. Change at least one input/parameter and explain the effect | Section **C** |
| D. Explain the output in words and interpret the graph | Section **D** |
| E. Modify the program for a different but related real-world case (assumptions, input data, output, interpretation) | Section **E** |

---

## Task index

| Task | Topic | Program | Documentation | Figure |
|---|---|---|---|---|
| 2 | NumPy arrays and numerical computation | [code](code/Task_02_numpy_arrays.py) | [docs](docs/Task_02_numpy_arrays.md) | – |
| 3 | Mathematical functions and vectorization | [code](code/Task_03_vectorization.py) | [docs](docs/Task_03_vectorization.md) | – |
| 4 | Floating-point arithmetic and numerical errors | [code](code/Task_04_numerical_errors.py) | [docs](docs/Task_04_numerical_errors.md) | – |
| 5 | Matrix algebra and matrix operations | [code](code/Task_05_matrix_algebra.py) | [docs](docs/Task_05_matrix_algebra.md) | [fig](figures/task05_transformations.png) |
| 6 | Solution of systems of linear equations | [code](code/Task_06_linear_systems.py) | [docs](docs/Task_06_linear_systems.md) | – |
| 7 | Gaussian elimination and LU decomposition | [code](code/Task_07_gaussian_lu.py) | [docs](docs/Task_07_gaussian_lu.md) | – |
| 8 | Iterative methods for linear systems | [code](code/Task_08_iterative_linear.py) | [docs](docs/Task_08_iterative_linear.md) | [fig](figures/task08_convergence.png) |
| 9 | Eigenvalues and eigenvectors | [code](code/Task_09_eigenvalues.py) | [docs](docs/Task_09_eigenvalues.md) | – |
| 10 | Root finding: bisection and fixed point | [code](code/Task_10_bisection_fixed_point.py) | [docs](docs/Task_10_bisection_fixed_point.md) | [fig](figures/task10_roots.png) |
| 11 | Root finding: Newton-Raphson and secant | [code](code/Task_11_newton_secant.py) | [docs](docs/Task_11_newton_secant.md) | – |
| 12 | Polynomial and nonlinear equation solving | [code](code/Task_12_nonlinear_equations.py) | [docs](docs/Task_12_nonlinear_equations.md) | [fig](figures/task12_intersections.png) |
| 13 | Interpolation | [code](code/Task_13_interpolation.py) | [docs](docs/Task_13_interpolation.md) | [fig](figures/task13_interpolation.png) |
| 14 | Curve fitting and approximation | [code](code/Task_14_curve_fitting.py) | [docs](docs/Task_14_curve_fitting.md) | [fig](figures/task14_curve_fit.png) |
| 15 | Numerical differentiation | [code](code/Task_15_numerical_differentiation.py) | [docs](docs/Task_15_numerical_differentiation.md) | [fig](figures/task15_differentiation.png) |
| 16 | Numerical integration | [code](code/Task_16_numerical_integration.py) | [docs](docs/Task_16_numerical_integration.md) | [fig](figures/task16_integration.png) |
| 17 | ODEs: Euler method | [code](code/Task_17_euler_ode.py) | [docs](docs/Task_17_euler_ode.md) | [fig](figures/task17_euler.png) |
| 18 | Numerical solution of ODEs using SciPy | [code](code/Task_18_scipy_ode.py) | [docs](docs/Task_18_scipy_ode.md) | [fig](figures/task18_ode.png) |
| 19 | Numerical optimization | [code](code/Task_19_optimization.py) | [docs](docs/Task_19_optimization.md) | – |
| 20 | Random numbers and Monte Carlo methods | [code](code/Task_20_monte_carlo.py) | [docs](docs/Task_20_monte_carlo.md) | [fig](figures/task20_monte_carlo.png) |

---

## How each program is organised

Every script has three clearly marked parts:

1. **PART 1: Original.** The program from the brief (with extra checks added).
2. **PART 2: Changed input.** One or more parameters changed, with the effect printed.
3. **PART 3: Related case.** A different real-world problem with its own assumptions and data.

Console output of each script is saved in `outputs/`. Figures are saved in `figures/` (no window pops up).

## Running

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
./run_all.sh                     # runs every task; or: python code/Task_10_bisection_fixed_point.py
```

Requires NumPy 2.0 or newer (Task 16 uses `np.trapezoid`). Timing results in Tasks 3 and 7 differ from machine to machine; the speed-up ratios are what matter. All random numbers use fixed seeds, so every other result is reproducible.

## Publishing to GitHub

```bash
git init
git add .
git commit -m "BIT 2118 Scientific Computing: tasks 2-20"
git branch -M main
git remote add origin https://github.com/<your-username>/bit2118-scientific-computing.git
git push -u origin main
```

Then submit the repository link and the documentation on VLMS.
