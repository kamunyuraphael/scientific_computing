# Task 12 – Polynomial and Nonlinear Equation Solving

**Program:** `code/Task_12_nonlinear_equations.py` · **Figure:** `figures/task12_intersections.png`

---

## B. Input values and mathematical operation

| Item | Detail |
|---|---|
| Equations | Circle x² + y² = 4 and parabola y = x² − 1, written as residuals that must both equal 0 |
| Solver | `scipy.optimize.root` from initial guesses [1, 1] and [−1, 1] |
| Extra | `np.roots([1, −5, 6])` solves the polynomial x² − 5x + 6 = 0 → 3 and 2 |

**Results:**

| Guess | Intersection | Residuals |
|---|---|---|
| [1, 1] | (1.51749, 1.30278) | about 2.5 × 10⁻¹³ |
| [−1, 1] | (−1.51749, 1.30278) | about 2.5 × 10⁻¹³ |

Exact check: y = (−1 + √13)/2 = 1.30278 and x = ±1.51749. Substituting y = x² − 1 into the circle gives y² + y − 3 = 0, which has a valid positive-y solution only.

## C. Parameter change

| Change | Result |
|---|---|
| Radius 1 (r² = 1) | Three intersections: (±1, 0) and (0, −1) |
| Radius 3 (r² = 9) | Two intersections: (±1.836, 2.372) |
| Radius 2, guess [1, −2] | Fails (`success = False`): no real intersection exists in the lower region |

**Explanation:** the number of intersections depends on the parameters, and the solver only finds the solution near its starting guess. Several different guesses are needed to find every root. A failed convergence (non-zero residual) is not an answer.

## D. Meaning of the output and graph

- **Graph:** the circle and the upward parabola cross at two black points, symmetric about the y-axis. The residuals near zero prove both equations are satisfied at those points.

## E. Related real-world case: finding a position from two distance beacons

**Assumptions:** beacon 1 at (0, 0) and beacon 2 at (6, 0) each measure a distance of 5 m to a device. Each distance defines a circle. A third beacon at (3, 8) measures 4 m.

**Output:**

| Case | Solution |
|---|---|
| Two beacons, guess [2, 3] | (3, 4) |
| Two beacons, guess [2, −3] | (3, −4) |
| Three beacons (least squares) | (3, 4), cost about 0 |

**Interpretation:** two circles intersect at two points, so two beacons give an ambiguous position (a mirror image). A third distance removes the ambiguity. This is why positioning systems such as GPS need at least three (in 3-D, four) satellites.
