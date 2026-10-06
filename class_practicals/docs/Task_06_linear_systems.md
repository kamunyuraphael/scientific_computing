# Task 6 – Solution of Systems of Linear Equations

**Program:** `code/Task_06_linear_systems.py` · **Output:** `outputs/Task_06_linear_systems.txt`

---

## B. Input values and mathematical operation

System Ax = b, with x = number of Type A servers and y = number of Type B servers:

- 4x + 2y = 20 (CPU units)
- 8x + 12y = 72 (memory in GB)

A = [[4, 2],[8, 12]], b = [20, 72]. Operation: `np.linalg.solve(A, b)`, then verify with A·x and the residual b − A·x.

**Result:** x = 3 Type A servers, y = 4 Type B servers. Residual norm 0. det(A) = 32, condition number 6.98 (well-conditioned).

## C. Parameter change

| Change | Result |
|---|---|
| Totals become 28 CPU and 96 GB | x = 4.5, y = 5.0 |
| Make A nearly singular (second row ≈ 2 × first row) | cond(A) = 2.5 × 10⁵; solution [5, 0]. Changing b by only 0.001 gives [0, 10] |

**Explanation:** x = 4.5 is not a whole number of servers, so the measured totals are inconsistent with a real server count, or the model is wrong. In the second change, a tiny change in b flips the answer completely. This is ill-conditioning: when rows are almost dependent, small measurement errors are hugely amplified.

## D. Meaning of the output

- 3 × (4,8) + 4 × (2,12) = (12+8, 24+48) = (20, 72), matching the observed usage exactly.
- Residual norm 0 means the computed solution reproduces b. Always check this.

## E. Related real-world case: mesh-current analysis of a three-loop circuit

**Assumptions:** Kirchhoff's voltage law gives R·I = V, with loop resistances (Ω) R = [[20, −5, 0],[−5, 25, −10],[0, −10, 30]] and loop voltage sources V = [12, 0, −6] V.

**Output:**

| Quantity | Value |
|---|---|
| I₁, I₂, I₃ | 0.61224 A, 0.04898 A, −0.18367 A |
| Residual norm | 9.2 × 10⁻¹⁶ |
| Current in the shared resistor (I₁ − I₂) | 0.56327 A |

**Interpretation:** I₃ is negative, so the real current flows opposite to the direction we assumed for loop 3. The tiny residual confirms the solution satisfies all three loop equations.
