"""Task 8 - Iterative Methods for Linear Systems
PART 1 original | PART 2 changed tolerance/boundaries | PART 3 related case (rod with n grid points)"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

def jacobi(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A); R = A - np.diagflat(D)
    x = np.zeros_like(b); errors = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x_new, errors
        x = x_new
    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b); errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x, errors
    return x, errors

def rod(n, left, right):
    A = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
    b = np.zeros(n); b[0] = left; b[-1] = right
    return A, b

print("=== PART 1: Original - 5 interior points, 100 C / 20 C ===")
A, b = rod(5, 100., 20.)
x_j, err_j = jacobi(A, b); x_gs, err_gs = gauss_seidel(A, b); x_exact = np.linalg.solve(A, b)
print("Jacobi temperatures:", x_j)
print("Gauss-Seidel temperatures:", x_gs)
print("Direct solution:", x_exact)
print("Iterations: Jacobi =", len(err_j), "| Gauss-Seidel =", len(err_gs))
print("Max error vs direct: Jacobi", np.max(np.abs(x_j-x_exact)), "| GS", np.max(np.abs(x_gs-x_exact)))

print("\n=== PART 2: Changed input - tolerance 1e-8 -> 1e-3, and boundaries 100/20 -> 150/30 ===")
_, e1 = jacobi(A, b, tol=1e-3); _, e2 = gauss_seidel(A, b, tol=1e-3)
print("tol=1e-3 iterations: Jacobi", len(e1), "| GS", len(e2))
A2, b2 = rod(5, 150., 30.)
xj2, ej2 = jacobi(A2, b2); xg2, eg2 = gauss_seidel(A2, b2)
print("Boundaries 150/30 -> GS temperatures:", np.round(xg2, 4), "| iterations J/GS:", len(ej2), len(eg2))

print("\n=== PART 3: Related case - metal rod, boundaries 150 C and 30 C, n points ===")
for n in (5, 10, 20, 40):
    An, bn = rod(n, 150., 30.)
    xj, ej = jacobi(An, bn, tol=1e-6, max_iter=20000)
    xg, eg = gauss_seidel(An, bn, tol=1e-6, max_iter=20000)
    print(f"n={n:3d}: Jacobi {len(ej):5d} iterations | Gauss-Seidel {len(eg):5d} iterations | max err GS {np.max(np.abs(xg-np.linalg.solve(An,bn))):.2e}")
An, bn = rod(10, 150., 30.)
xg, _ = gauss_seidel(An, bn, tol=1e-10, max_iter=20000)
print("10-point profile (GS):", np.round(xg, 3))
# note: right-hand side b holds boundary temperatures *as given* (b[0]=T_left, b[-1]=T_right) following the brief's model.

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].semilogy(err_j, label="Jacobi"); ax[0].semilogy(err_gs, label="Gauss-Seidel")
ax[0].set_xlabel("Iteration"); ax[0].set_ylabel("Maximum change"); ax[0].set_title("Convergence (original, 5 points)")
ax[0].legend(); ax[0].grid(True)
ax[1].plot(range(1, 11), xg, "o-"); ax[1].set_xlabel("Grid point"); ax[1].set_ylabel("Temperature (C)")
ax[1].set_title("Related case: 10-point rod profile"); ax[1].grid(True)
plt.tight_layout(); plt.savefig(os.path.join(FIG, "task08_convergence.png"), dpi=130); plt.close()
