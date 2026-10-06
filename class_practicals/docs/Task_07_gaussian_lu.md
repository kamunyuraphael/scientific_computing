# Task 7 – Gaussian Elimination and LU Decomposition

**Program:** `code/Task_07_gaussian_lu.py` · **Output:** `outputs/Task_07_gaussian_lu.txt`

> Timings depend on the computer. The speed-up ratio is the meaningful figure.

---

## B. Input values and mathematical operation

| Item | Detail |
|---|---|
| Matrix A | [[4, −1, 0],[−1, 4, −1],[0, −1, 3]] (same every time) |
| Vectors b | Three measurement sets: [15,10,10], [16,11,9], [14,12,11] |
| Operation | Factor once: PA = LU (`lu_factor`). Then for each b: forward substitution Ly = Pb, back substitution Ux = y (`lu_solve`) |

The script also contains a hand-written Gaussian elimination with partial pivoting, which gives the same answer as SciPy.

**Results:**

| Set | Solution x |
|---|---|
| 1 | [5, 5, 5] |
| 2 | [5.3171, 5.2683, 4.7561] |
| 3 | [4.9024, 5.6098, 5.5366] |

Elimination multipliers in L are −0.25 and −0.2667, and the diagonal of U is 4, 3.75, 2.7333. `P @ L @ U` reproduces A (check = True).

## C. Parameter change

**Change:** last diagonal entry reduced from 3 to 0.9 (weaker diagonal dominance).

| Quantity | Original | Changed |
|---|---|---|
| Condition number | 2.39 | 8.83 |
| Solution for set 1 | [5, 5, 5] | [6.105, 9.421, 21.579] |

**Explanation:** a smaller last pivot means more amplification. The third unknown more than quadruples. Also tested: a matrix with a zero in position (0,0) fails without row swapping but works with pivoting, giving [0.667, 1.667, 0.667].

## D. Meaning of the output

- Solution [5, 5, 5] for set 1 can be checked: 4·5 − 5 = 15, −5 + 20 − 5 = 10, −5 + 15 = 10, which equals b.
- Residual norms are about 10⁻¹⁵, meaning the factorization solved the system to machine precision.

## E. Related real-world case: resistor ladder with 2000 changing sources

**Assumptions:** a 300-node ladder network gives a tridiagonal matrix (diagonal 3, off-diagonals −1) that never changes. 2000 different source vectors b (uniform 0 to 10, seed 1) arrive one after another.

**Output:**

| Method | Time |
|---|---|
| Full solve for every b | 2.00 s |
| Factor once, reuse (LU) | 0.064 s |
| Speed-up | about 31× |
| Largest residual (first 200 solves) | 2.9 × 10⁻¹⁴ |

**Interpretation:** factorization costs O(n³) but each reuse costs only O(n²). When A is constant (as in a real-time simulation), factoring once is far cheaper, with no loss of accuracy.
