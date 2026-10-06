# Task 5 – Matrix Algebra and Matrix Operations

**Program:** `code/Task_05_matrix_algebra.py` · **Figure:** `figures/task05_transformations.png`

---

## B. Input values and mathematical operation

| Item | Detail |
|---|---|
| Input | Unit square with corners (0,0), (1,0), (1,1), (0,1); rotation 45°; scaling factors (2, 1.5) |
| Matrices | Rotation R = [[cos θ, −sin θ],[sin θ, cos θ]], Scale S = diag(2, 1.5) |
| Operation | Combined T = R·S; points transformed by P·Tᵀ (matrix multiplication); determinant det(T) |

Result: T = [[1.4142, −1.0607],[1.4142, 1.0607]] and det(T) = 3.0.

## C. Parameter change

| Change | Result |
|---|---|
| Angle 90°, scale (1, 1) | Corners become (0,0), (0,1), (−1,1), (−1,0). det = 1 |
| Scale (2, 0) with 45° | All points collapse onto a line. det = 0 (singular, not invertible) |

**Explanation:** a pure rotation only turns the shape, so area and determinant stay 1. Scaling by zero in one direction destroys a dimension. The determinant 0 signals that no inverse exists.

## D. Meaning of the output

- det(T) = 3.0 = 2 × 1.5 × 1: the shape's area is multiplied by 3 (rotation does not change area).
- Transformed corners: (0,0), (1.414,1.414), (0.354,2.475), (−1.061,1.061). The figure shows the original square and the larger, tilted parallelogram.

## E. Related real-world case: reflect and shear a 2-D part in CAD

**Assumptions:** a triangle with vertices (0,0), (4,0), (2,3) is first mirrored across the y-axis, then sheared by 0.5 in the x-direction. M = Shear · Reflect.

**Output:**

| Quantity | Value |
|---|---|
| M | [[−1, 0.5],[0, 1]] |
| New triangle | (0,0), (−4,0), (−0.5,3) |
| det(M) | −1 |
| Recovered with M⁻¹ | (0,0), (4,0), (2,3) (original) |

**Interpretation:** |det| = 1 means area is preserved (reflection and shear do not change area). The negative sign means orientation is flipped, which is exactly what a mirror does. The inverse matrix undoes the transformation, which confirms AA⁻¹ = I.
