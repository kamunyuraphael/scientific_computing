"""Task 4 - Floating-Point Arithmetic and Numerical Errors
PART 1 original | PART 2 changed approximation | PART 3 related case (banking accumulation)"""
import math
import numpy as np

print("=== PART 1: Original ===")
calculated = 0.1 + 0.2
expected = 0.3
print("0.1 + 0.2 =", calculated)
print("Exact comparison:", calculated == expected)
print("Tolerance-based comparison:", np.isclose(calculated, expected))
true_value = np.sqrt(2)
approx_value = 1.414
absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)
print(f"Absolute error: {absolute_error:.8f}")
print(f"Relative error: {relative_error:.8%}")
for x in [1e-4, 1e-8, 1e-12]:
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)
    print(f"x={x:.0e}: direct={direct:.12f}, stable={stable:.12f}")

print("\n=== PART 2: Changed input - approximation 1.414 -> 1.41421 and extra x values ===")
for approx in (1.414, 1.4142, 1.41421):
    ae = abs(np.sqrt(2) - approx)
    print(f"approx={approx}: abs err={ae:.2e}, rel err={ae/np.sqrt(2):.4%}")
for x in [1e-14, 1e-16]:
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)
    print(f"x={x:.0e}: direct={direct:.12f}, stable={stable:.12f}")

print("\n=== PART 3: Related case - banking: adding 0.10 one million times ===")
naive = 0.0
for _ in range(1_000_000):
    naive += 0.10
exact_total = 100_000.0
print(f"Naive float sum   : {naive:.10f}")
print(f"math.fsum         : {math.fsum([0.10]*1_000_000):.10f}")
print(f"Expected          : {exact_total:.10f}")
print(f"Naive abs error   : {abs(naive-exact_total):.3e}")
print("Naive == expected :", naive == exact_total, "| np.isclose:", np.isclose(naive, exact_total))
from decimal import Decimal
print("Decimal sum       :", sum([Decimal('0.10')]*1_000_000))
