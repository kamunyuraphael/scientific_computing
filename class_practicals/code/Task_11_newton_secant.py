"""Task 11 - Root Finding: Newton-Raphson and Secant
PART 1 original | PART 2 changed cash flows/start | PART 3 related case (loan APR)"""
import numpy as np
from scipy.optimize import root_scalar

def make_npv(cash_flows):
    def npv(rate): return sum(cf / (1 + rate)**t for t, cf in enumerate(cash_flows))
    def d_npv(rate): return sum(-t * cf / (1 + rate)**(t + 1) for t, cf in enumerate(cash_flows) if t > 0)
    return npv, d_npv

def newton_manual(f, df, x0, tol=1e-12, max_iter=50):
    x = x0; hist = [x]
    for _ in range(max_iter):
        xn = x - f(x)/df(x); hist.append(xn)
        if abs(xn - x) < tol: break
        x = xn
    return hist

print("=== PART 1: Original ===")
cash_flows = [-10000, 3000, 3500, 4000, 2500]
npv, d_npv = make_npv(cash_flows)
newton = root_scalar(npv, fprime=d_npv, x0=0.10, method="newton", xtol=1e-12)
secant = root_scalar(npv, x0=0.05, x1=0.20, method="secant", xtol=1e-12)
print(f"IRR using Newton-Raphson: {newton.root:.6%}")
print(f"IRR using Secant method: {secant.root:.6%}")
print(f"NPV at Newton solution: {npv(newton.root):.6f}")
print("Newton iterations (scipy):", newton.iterations, "| Secant iterations:", secant.iterations)
h = newton_manual(npv, d_npv, 0.10)
print("Manual Newton iterates:", [f"{v:.8f}" for v in h])
print("Textbook check, f(x)=x^2-2 from x0=1.5:", [round(v, 6) for v in newton_manual(lambda x: x*x-2, lambda x: 2*x, 1.5)])

print("\n=== PART 2: Changed input - larger final cash flow and different start ===")
cf2 = [-10000, 3000, 3500, 4000, 5500]
npv2, d2 = make_npv(cf2)
n2 = root_scalar(npv2, fprime=d2, x0=0.10, method="newton", xtol=1e-12)
print(f"IRR with final inflow 5500: {n2.root:.4%} (was {newton.root:.4%})")
import warnings
warnings.filterwarnings("ignore")
for x0 in (0.10, 0.50, 2.0):
    r = root_scalar(npv, fprime=d_npv, x0=x0, method="newton", xtol=1e-12)
    ok = abs(npv(r.root)) < 1e-6 and r.root > -1
    if ok:
        print(f"Start x0={x0}: root {r.root:.6%} in {r.iterations} iterations")
    else:
        print(f"Start x0={x0}: Newton DIVERGED (|NPV| at 'root' is not ~0) - a poor start can fail")

print("\n=== PART 3: Related case - loan APR from payment ===")
# Loan of 12,000 repaid with 36 monthly payments of 380. Find monthly rate r.
P, pay, n = 12000.0, 380.0, 36
def f(r): return P - pay * (1 - (1 + r)**(-n)) / r
def df(r):
    return -pay * (n*(1+r)**(-n-1)/r - (1 - (1+r)**(-n))/r**2)
nw = root_scalar(f, fprime=df, x0=0.02, method="newton", xtol=1e-14)
sc = root_scalar(f, x0=0.005, x1=0.03, method="secant", xtol=1e-14)
print(f"Monthly rate (Newton): {nw.root:.6%} in {nw.iterations} iterations")
print(f"Monthly rate (Secant): {sc.root:.6%} in {sc.iterations} iterations")
print(f"Nominal APR = 12 x monthly = {12*nw.root:.4%}")
print(f"Effective annual rate = {(1+nw.root)**12-1:.4%}")
print(f"Total repaid {pay*n:.0f} -> interest cost {pay*n-P:.0f}")
print(f"Check payment at root: {P*nw.root/(1-(1+nw.root)**-n):.6f}")
