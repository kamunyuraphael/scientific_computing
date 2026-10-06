"""Task 7 - Gaussian Elimination and LU Decomposition
PART 1 original | PART 2 changed matrix | PART 3 related case (resistor network, 2000 source vectors, timing)"""
import time
import numpy as np
from scipy.linalg import lu_factor, lu_solve, lu

def gauss_elimination(A, b):
    """Gaussian elimination with partial pivoting + back-substitution (written out for the report)."""
    A = A.astype(float).copy(); b = b.astype(float).copy(); n = len(b)
    for k in range(n - 1):
        p = np.argmax(np.abs(A[k:, k])) + k
        if p != k:
            A[[k, p]] = A[[p, k]]; b[[k, p]] = b[[p, k]]
        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]
            A[i, k:] -= m * A[k, k:]
            b[i] -= m * b[k]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - A[i, i+1:] @ x[i+1:]) / A[i, i]
    return x

print("=== PART 1: Original ===")
A = np.array([[4.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 3.0]])
measurement_sets = [np.array([15.0, 10.0, 10.0]), np.array([16.0, 11.0, 9.0]), np.array([14.0, 12.0, 11.0])]
lu_, piv = lu_factor(A)
for i, b in enumerate(measurement_sets, start=1):
    x = lu_solve((lu_, piv), b)
    residual = b - A @ x
    print(f"Measurement set {i}")
    print("Solution:", x)
    print("Residual norm:", np.linalg.norm(residual))
    print()
print("Direct solution for first set:", np.linalg.solve(A, measurement_sets[0]))
print("Hand-written Gaussian elimination, first set:", gauss_elimination(A, measurement_sets[0]))
P, L, U = lu(A)
print("L =\n", np.round(L, 4)); print("U =\n", np.round(U, 4))
print("Check P@L@U == A:", np.allclose(P @ L @ U, A))

print("\n=== PART 2: Changed input - last diagonal 3 -> 0.9 (weaker diagonal dominance) ===")
A2 = A.copy(); A2[2, 2] = 0.9
A2[1, 2] = -1.0; A2[2, 1] = -1.0
print("cond(A) =", round(np.linalg.cond(A), 2), "| cond(A2, last diagonal=0.9) =", round(np.linalg.cond(A2), 2))
print("Solution A :", np.linalg.solve(A, measurement_sets[0]))
print("Solution A2:", np.linalg.solve(A2, measurement_sets[0]))
A_swap = np.array([[0.0, 2.0, 1.0], [1.0, 1.0, 1.0], [2.0, 1.0, 0.0]])
print("Zero pivot in position (0,0) handled by pivoting:", np.linalg.solve(A_swap, np.array([4.0, 3.0, 3.0])))

print("\n=== PART 3: Related case - 300-node resistor ladder, 2000 changing source vectors ===")
n = 300
A_l = np.diag(np.full(n, 3.0)) + np.diag(np.full(n-1, -1.0), 1) + np.diag(np.full(n-1, -1.0), -1)
rng = np.random.default_rng(1)
B = rng.uniform(0, 10, (2000, n))
t0 = time.perf_counter()
for b in B:
    np.linalg.solve(A_l, b)
t_repeat = time.perf_counter() - t0
t0 = time.perf_counter()
lu_l, piv_l = lu_factor(A_l)
X = [lu_solve((lu_l, piv_l), b) for b in B]
t_lu = time.perf_counter() - t0
print(f"Repeated full solves : {t_repeat:.3f} s")
print(f"Factor once + reuse  : {t_lu:.3f} s  (speed-up {t_repeat/t_lu:.1f}x)")
print("Max residual norm over the first 200 solves:", max(np.linalg.norm(b - A_l @ x) for b, x in zip(B[:200], X[:200])))
