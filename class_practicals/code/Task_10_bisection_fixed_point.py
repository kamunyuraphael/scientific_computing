"""Task 10 - Root Finding: Bisection and Fixed-Point
PART 1 original | PART 2 changed constants | PART 3 related case (profit break-even points)"""
import numpy as np
from scipy.optimize import root_scalar
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

def bisect_manual(f, a, b, tol=1e-10):
    n = 0
    while (b - a) / 2 > tol:
        m = (a + b) / 2
        if f(a) * f(m) <= 0: b = m
        else: a = m
        n += 1
    return (a + b) / 2, n

def fixed_point(g, x0, tol=1e-10, max_iter=1000):
    x = x0; hist = [x]
    for _ in range(max_iter):
        xn = g(x); hist.append(xn)
        if abs(xn - x) < tol: break
        x = xn
    return hist

print("=== PART 1: Original ===")
def heat_balance(T): return T - 25 - 10*np.exp(-T/20)
solution = root_scalar(heat_balance, bracket=[20, 40], method="bisect", xtol=1e-10)
def g(T): return 25 + 10*np.exp(-T/20)
history = fixed_point(g, 30.0)
print(f"Bisection equilibrium temperature: {solution.root:.6f} C")
print(f"Fixed-point equilibrium temperature: {history[-1]:.6f} C")
print("Fixed-point iterations:", len(history) - 1)
r, n = bisect_manual(heat_balance, 20, 40)
print(f"Hand-written bisection: {r:.6f} C after {n} halvings (bracket width 20 -> {20/2**n:.2e})")
print("|g'(T*)| =", abs(-0.5*np.exp(-solution.root/20)), "< 1  -> fixed-point converges")

print("\n=== PART 2: Changed input - ambient 25 -> 35 C and heat-source 10 -> 40 ===")
def hb2(T, amb=35, src=40): return T - amb - src*np.exp(-T/20)
s2 = root_scalar(hb2, bracket=[20, 80], method="bisect", xtol=1e-10)
h2 = fixed_point(lambda T: 35 + 40*np.exp(-T/20), 30.0)
print(f"New equilibrium (bisection): {s2.root:.6f} C | fixed-point: {h2[-1]:.6f} C | iterations {len(h2)-1}")
print("|g'| at root =", round(abs(-2*np.exp(-s2.root/20)), 4))
_, n_tight = bisect_manual(heat_balance, 20, 40, 1e-4)
_, n_loose = bisect_manual(heat_balance, 20, 40, 1e-12)
print(f"Halvings for tol 1e-4: {n_tight} | tol 1e-12: {n_loose}")

print("\n=== PART 3: Related case - break-even points of profit(q) = 300*sqrt(q) - 4000 - 5q ===")
def profit(q): return 300*np.sqrt(q) - 4000 - 5*q
lo = root_scalar(profit, bracket=[100, 1000], method="bisect", xtol=1e-9)
hi = root_scalar(profit, bracket=[1000, 2500], method="bisect", xtol=1e-9)
print(f"Lower break-even: {lo.root:.4f} units | Upper break-even: {hi.root:.4f} units")
print(f"Profit at 400: {profit(400):.4f} | at 1600: {profit(1600):.4f} | at 1000 (between): {profit(1000):.2f}")
q_best = 900  # maximiser: d/dq = 150/sqrt(q) - 5 = 0
print(f"Maximum profit at q={q_best}: {profit(q_best):.2f}")

temps = np.linspace(20, 40, 300)
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].plot(temps, heat_balance(temps)); ax[0].axhline(0, lw=0.8); ax[0].axvline(solution.root, ls="--")
ax[0].set_xlabel("Temperature (C)"); ax[0].set_ylabel("Heat-balance function"); ax[0].set_title("Equilibrium temperature"); ax[0].grid(True)
q = np.linspace(50, 2500, 400)
ax[1].plot(q, profit(q)); ax[1].axhline(0, lw=0.8)
ax[1].axvline(lo.root, ls="--", c="g"); ax[1].axvline(hi.root, ls="--", c="r")
ax[1].set_xlabel("Units sold"); ax[1].set_ylabel("Profit"); ax[1].set_title("Related case: two break-even points"); ax[1].grid(True)
plt.tight_layout(); plt.savefig(os.path.join(FIG, "task10_roots.png"), dpi=130); plt.close()
