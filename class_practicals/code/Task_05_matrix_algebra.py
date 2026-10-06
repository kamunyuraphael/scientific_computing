"""Task 5 - Matrix Algebra and Matrix Operations
PART 1 original | PART 2 changed angle/scale | PART 3 related case (reflect + shear triangle)"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

def transform(points, angle_deg, sx, sy):
    a = np.deg2rad(angle_deg)
    rotation = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
    scale = np.array([[sx, 0.0], [0.0, sy]])
    T = rotation @ scale
    return T, points @ T.T

points = np.array([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]])

print("=== PART 1: Original - rotate 45 deg, scale (2, 1.5) ===")
T, out = transform(points, 45, 2.0, 1.5)
print("Original points:\n", points)
print("Transformation matrix:\n", T)
print("Transformed points:\n", out)
print("Determinant:", np.linalg.det(T))

print("\n=== PART 2: Changed input - rotate 90 deg, scale (1, 1) then (2, 0) ===")
T2, out2 = transform(points, 90, 1.0, 1.0)
print("90 deg rotation only:\n", np.round(out2, 6), "\nDeterminant:", round(np.linalg.det(T2), 6))
T3, out3 = transform(points, 45, 2.0, 0.0)
print("Scale y by 0 (singular):\n", np.round(out3, 4), "\nDeterminant:", round(np.linalg.det(T3), 12))

print("\n=== PART 3: Related case - reflect a triangle in the y-axis then shear ===")
tri = np.array([[0.0, 0.0], [4.0, 0.0], [2.0, 3.0]])
reflect_y = np.array([[-1.0, 0.0], [0.0, 1.0]])
shear = np.array([[1.0, 0.5], [0.0, 1.0]])
M = shear @ reflect_y
new_tri = tri @ M.T
print("Combined matrix M = shear @ reflect:\n", M)
print("New triangle:\n", new_tri)
print("det(M) =", np.linalg.det(M), "(negative => orientation flipped)")
back = new_tri @ np.linalg.inv(M).T
print("Recovered with inverse:\n", back)
print("AA^-1 = I check:", np.allclose(M @ np.linalg.inv(M), np.eye(2)))

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
for a_, pts, new, title in ((ax[0], points, out, "Square: rotate 45 + scale"), (ax[1], tri, new_tri, "Triangle: reflect + shear")):
    a_.fill(*np.vstack([pts, pts[:1]]).T, alpha=0.3, label="original")
    a_.fill(*np.vstack([new, new[:1]]).T, alpha=0.3, label="transformed")
    a_.set_aspect("equal"); a_.grid(True); a_.legend(); a_.set_title(title)
plt.tight_layout(); plt.savefig(os.path.join(FIG, "task05_transformations.png"), dpi=130); plt.close()
