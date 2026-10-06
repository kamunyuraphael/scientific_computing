# Task 8 – Iterative Methods for Linear Systems

**Program:** `code/Task_08_iterative_linear.py` · **Figure:** `figures/task08_convergence.png`

---

## B. Input values and mathematical operation

| Item | Detail |
|---|---|
| Matrix A | 5×5 tridiagonal: 2 on the diagonal, −1 on both neighbours |
| Vector b | [100, 0, 0, 0, 20] (boundary influence: left 100 °C, right 20 °C) |
| Start | x = 0, tolerance 10⁻⁸ |
| Jacobi | xᵢ⁽ᵏ⁺¹⁾ = (bᵢ − Σⱼ≠ᵢ aᵢⱼ xⱼ⁽ᵏ⁾) / aᵢᵢ, using only old values |
| Gauss-Seidel | Same formula but uses new values as soon as they are computed |

**Results:** both methods give [86.667, 73.333, 60.000, 46.667, 33.333] °C, matching the direct solution to about 3 × 10⁻⁸. Jacobi needed 150 iterations; Gauss-Seidel needed 75.

## C. Parameter change

| Change | Jacobi iterations | Gauss-Seidel iterations |
|---|---|---|
| Tolerance 10⁻⁸ (original) | 150 | 75 |
| Tolerance 10⁻³ | 70 | 35 |
| Boundaries 150/30 °C (tol 10⁻⁸) | 152 | 77 |

With boundaries 150/30 the temperatures become [130, 110, 90, 70, 50] °C.

**Explanation:** a looser tolerance stops earlier. Gauss-Seidel always needs about half as many iterations as Jacobi because it reuses fresh values. Changing the boundary temperatures changes the answer but barely changes the iteration count, since convergence speed is set by the matrix A, not by b.

## D. Meaning of the output and graph

- The temperatures fall in an even line from hot end to cold end: steady heat conduction.
- **Graph (left):** the y-axis is logarithmic, so the straight descending lines mean the error shrinks by a constant factor each iteration. The Gauss-Seidel line is steeper (faster). Both pass the tolerance line 10⁻⁸ at the iterations noted above.

## E. Related real-world case: metal rod with a variable number of grid points

**Assumptions:** same heat-conduction model, boundaries 150 °C and 30 °C, tolerance 10⁻⁶, n interior points.

| n | Jacobi iterations | Gauss-Seidel iterations |
|---|---|---|
| 5 | 120 | 61 |
| 10 | 385 | 194 |
| 20 | 1299 | 655 |
| 40 | 4506 | 2278 |

10-point profile (°C): 139.1, 128.2, 117.3, 106.4, 95.5, 84.5, 73.6, 62.7, 51.8, 40.9.

**Interpretation:** doubling the grid points multiplies the iterations by about 3.4. Finer grids give more detail but converge much more slowly, which is why large simulations use faster methods (for example conjugate gradient or multigrid). The right-hand graph shows the straight-line temperature profile.
