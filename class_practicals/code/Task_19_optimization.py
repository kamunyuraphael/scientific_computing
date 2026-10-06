"""Task 19 - Numerical Optimization
PART 1 original | PART 2 changed costs/requirement | PART 3 related case (maximise factory profit)"""
import numpy as np
from scipy.optimize import minimize

def solve_cloud(cost_a=12, cost_b=18, cap_a=100, cap_b=170, required=1000):
    cost = lambda z: cost_a*z[0] + cost_b*z[1]
    cons = {"type": "ineq", "fun": lambda z: cap_a*z[0] + cap_b*z[1] - required}
    sol = minimize(cost, x0=[5, 3], method="SLSQP", bounds=[(0, None), (0, None)], constraints=cons)
    best = None
    for a in range(0, 40):
        for b in range(0, 40):
            if cap_a*a + cap_b*b >= required:
                c_ = cost_a*a + cost_b*b
                if best is None or c_ < best[0]:
                    best = (c_, a, b, cap_a*a + cap_b*b)
    return sol, best

print("=== PART 0: f(x) = (x-3)^2 + 2 ===")
r = minimize(lambda x: (x[0]-3)**2 + 2, x0=[0.0])
print("Minimum at x =", np.round(r.x, 6), "| value =", round(r.fun, 6))

print("\n=== PART 1: Original ===")
solution, best_integer = solve_cloud()
x, y = solution.x
print("Optimization success:", solution.success)
print(f"Type A allocation: {x:.3f}")
print(f"Type B allocation: {y:.3f}")
print(f"Total capacity: {100*x + 170*y:.2f}")
print(f"Minimum planning cost: {solution.fun:.2f}")
print("Best nearby integer solution (cost, A, B, capacity):", best_integer)
print(f"Cost per capacity unit: A = {12/100:.4f}, B = {18/170:.4f} -> B is cheaper per unit of capacity")

print("\n=== PART 2: Changed input - Type B cost 18 -> 24 and requirement 1000 -> 1500 ===")
s2, b2 = solve_cloud(cost_b=24)
print(f"cost_B=24: A={s2.x[0]:.3f}, B={s2.x[1]:.3f}, cost {s2.fun:.2f} | integer best {b2}  (cost per unit B = {24/170:.4f} > A {0.12:.4f})")
s3, b3 = solve_cloud(required=1500)
print(f"required=1500: A={s3.x[0]:.3f}, B={s3.x[1]:.3f}, cost {s3.fun:.2f} | integer best {b3}")

print("\n=== PART 3: Related case - maximise factory profit ===")
# x = tables, y = chairs; profit 40 and 30; machine hours 2x + y <= 100; labour x + y <= 80; x <= 40
neg_profit = lambda z: -(40*z[0] + 30*z[1])
cons = [
    {"type": "ineq", "fun": lambda z: 100 - (2*z[0] + z[1])},
    {"type": "ineq", "fun": lambda z: 80 - (z[0] + z[1])},
]
sol = minimize(neg_profit, x0=[10, 10], method="SLSQP", bounds=[(0, 40), (0, None)], constraints=cons)
x, y = sol.x
print("Success:", sol.success)
print(f"Tables = {x:.3f}, Chairs = {y:.3f}, Max profit = {-sol.fun:.2f}")
print(f"Machine hours used: {2*x+y:.2f}/100 | labour used: {x+y:.2f}/80 | tables limit: {x:.2f}/40")
print("Both machine and labour constraints are active (binding); the table-limit is slack.")
best = max(((40*a + 30*b, a, b) for a in range(0, 41) for b in range(0, 81) if 2*a + b <= 100 and a + b <= 80))
print("Integer check (profit, tables, chairs):", best)
sol2 = minimize(neg_profit, x0=[10, 10], method="SLSQP", bounds=[(0, 40), (0, None)],
                constraints=[{"type": "ineq", "fun": lambda z: 120 - (2*z[0] + z[1])}, cons[1]])
print(f"If machine hours rise 100 -> 120: tables {sol2.x[0]:.2f}, chairs {sol2.x[1]:.2f}, profit {-sol2.fun:.2f} (gain {-sol2.fun+sol.fun:.2f} for 20 extra hours)")
