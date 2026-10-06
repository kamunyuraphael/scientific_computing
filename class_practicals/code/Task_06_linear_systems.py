"""Task 6 - Solution of Systems of Linear Equations
PART 1 original | PART 2 changed totals | PART 3 related case (3-loop circuit)"""
import numpy as np

print("=== PART 1: Original - servers ===")
A = np.array([[4.0, 2.0], [8.0, 12.0]])
b = np.array([20.0, 72.0])
solution = np.linalg.solve(A, b)
residual = b - A @ solution
print(f"Type A servers: {solution[0]:.0f}")
print(f"Type B servers: {solution[1]:.0f}")
print("Verification A @ solution:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))
print("det(A) =", np.linalg.det(A), "| cond(A) =", round(np.linalg.cond(A), 2))

print("\n=== PART 2: Changed input - totals become 28 CPU and 96 GB ===")
b2 = np.array([28.0, 96.0])
s2 = np.linalg.solve(A, b2)
print("Solution (A, B):", s2, "| residual norm:", np.linalg.norm(b2 - A @ s2))
print("\nChanged to an inconsistent/near-singular system (row 2 = 2 x row 1 + tiny change):")
A3 = np.array([[4.0, 2.0], [8.0, 4.0001]])
b3 = np.array([20.0, 40.0])
print("cond(A3) =", f"{np.linalg.cond(A3):.3e}", "| solution:", np.linalg.solve(A3, b3))
b3b = np.array([20.0, 40.001])
print("Tiny change in b ->", np.linalg.solve(A3, b3b))

print("\n=== PART 3: Related case - mesh-current analysis of a 3-loop circuit ===")
# Loop equations (Kirchhoff voltage law), resistances in ohms, sources in volts
R = np.array([
    [ 20.0, -5.0,  0.0],
    [ -5.0, 25.0, -10.0],
    [  0.0, -10.0, 30.0]
])
V = np.array([12.0, 0.0, -6.0])
I = np.linalg.solve(R, V)
print("Mesh currents I1, I2, I3 (A):", np.round(I, 5))
print("Verification R @ I =", np.round(R @ I, 10))
print("Residual norm:", np.linalg.norm(V - R @ I))
print("Current through shared resistor R12 (I1-I2):", round(I[0]-I[1], 5), "A")
