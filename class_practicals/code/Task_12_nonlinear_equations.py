"""Task 12 - Polynomial and Nonlinear Equation Solving
PART 1 original | PART 2 changed radius / guesses | PART 3 related case (2-beacon position fix)"""
import numpy as np
from scipy.optimize import root
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

print("=== PART 0: Polynomial x^2 - 5x + 6 = 0 ===")
print("np.roots:", np.roots([1, -5, 6]))

def make_eq(r2):
    def equations(z):
        x, y = z
        return [x**2 + y**2 - r2, y - (x**2 - 1)]
    return equations

print("\n=== PART 1: Original - circle r=2 and parabola y=x^2-1 ===")
equations = make_eq(4)
for guess in ([1.0, 1.0], [-1.0, 1.0]):
    sol = root(equations, guess)
    print("Initial guess:", guess); print("Intersection:", sol.x)
    print("Residuals:", [float(f"{r:.2e}") for r in equations(sol.x)]); print("Converged:", sol.success); print()
sol = root(equations, [1.0, -2.0])
print("Guess [1,-2] (lower region; no real intersection exists there):", np.round(sol.x, 4), "| residuals", np.round(equations(sol.x), 6), "| success:", sol.success)
print("Exact check: y = (-1+sqrt(13))/2 =", (-1 + np.sqrt(13))/2, "; x = +/-", np.sqrt((-1 + np.sqrt(13))/2 + 1))

print("\n=== PART 2: Changed input - circle radius 2 -> 1 (r^2 = 1), then 3 ===")
for r2 in (1, 9):
    eq = make_eq(r2)
    found = set()
    for g in ([1, 1], [-1, 1], [1, -2], [-1, -2], [0.5, 0], [2, 3]):
        s = root(eq, g)
        if s.success and np.linalg.norm(eq(s.x)) < 1e-9:
            found.add(tuple(float(v) for v in np.round(s.x, 5)))
    print(f"r^2 = {r2}: intersections found -> {sorted(found)}")

print("\n=== PART 3: Related case - 2-beacon position fix (trilateration) ===")
# Beacon 1 at (0,0), distance 5; beacon 2 at (6,0), distance 5.
def beacons(z):
    x, y = z
    return [x**2 + y**2 - 5.0**2, (x - 6.0)**2 + y**2 - 5.0**2]
for guess in ([2.0, 3.0], [2.0, -3.0]):
    s = root(beacons, guess)
    print("Guess", guess, "->", np.round(s.x, 6), "| residuals", np.round(beacons(s.x), 10))
print("Ambiguity: two beacons give TWO candidate positions; a third beacon is needed.")
def beacons3(z):
    x, y = z
    return [x**2 + y**2 - 25.0, (x - 6.0)**2 + y**2 - 25.0, (x - 3.0)**2 + (y - 8.0)**2 - 16.0]
from scipy.optimize import least_squares
ls = least_squares(beacons3, [2.0, -3.0])
print("Third beacon at (3,8), dist 4 -> least-squares fix:", np.round(ls.x, 4), "cost", round(ls.cost, 6))
ls2 = least_squares(beacons3, [2.0, 3.0])
print("From the upper guess:", np.round(ls2.x, 4), "cost", f"{ls2.cost:.2e}")

t = np.linspace(0, 2*np.pi, 400); xs = np.linspace(-2.5, 2.5, 400)
plt.figure(figsize=(5.5, 5.5))
plt.plot(2*np.cos(t), 2*np.sin(t), label="Circle r=2"); plt.plot(xs, xs**2 - 1, label="y = x^2 - 1")
pts = []
for g in ([1.0, 1.0], [-1.0, 1.0]): pts.append(root(equations, g).x)
pts = np.array(pts); plt.scatter(pts[:, 0], pts[:, 1], c="k", zorder=5, label="Intersections")
plt.ylim(-3, 3); plt.gca().set_aspect("equal"); plt.grid(True); plt.legend()
plt.title("Circle-parabola intersections"); plt.savefig(os.path.join(FIG, "task12_intersections.png"), dpi=130); plt.close()
