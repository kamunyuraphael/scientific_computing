"""Task 16 - Numerical Integration
PART 1 original | PART 2 changed sampling | PART 3 related case (water flow with known exact volume)"""
import numpy as np
from scipy.integrate import simpson, quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

print("=== PART 1: Original - smart meter ===")
time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
power_kw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])
energy_trapezoid = np.trapezoid(power_kw, time_hours)
energy_simpson = simpson(power_kw, x=time_hours)
print(f"Energy using trapezoidal rule: {energy_trapezoid:.3f} kWh")
print(f"Energy using Simpson's rule: {energy_simpson:.3f} kWh")
print(f"Difference between estimates: {abs(energy_simpson-energy_trapezoid):.3f} kWh")
print("Constant 2 kW for 3 h:", np.trapezoid([2, 2], [0, 3]), "kWh")

print("\n=== PART 2: Changed input - readings every 4 h (sub-sample) and a spike at 6 h (1.8 -> 3.0) ===")
t4, p4 = time_hours[::2], power_kw[::2]
print(f"Every 4 h: trapezoid {np.trapezoid(p4, t4):.3f} | Simpson {simpson(p4, x=t4):.3f} kWh")
p_spike = power_kw.copy(); p_spike[3] = 3.0
print(f"Spike at 6 h: trapezoid {np.trapezoid(p_spike, time_hours):.3f} | Simpson {simpson(p_spike, x=time_hours):.3f} kWh")

print("\n=== PART 3: Related case - water flow Q(t) = 5 + 3 sin(pi t / 6) L/s, t in [0,12] h -> exact volume known ===")
# t in hours; Q in litres/second. Volume in litres = integral Q dt * 3600
Q = lambda t: 5 + 3*np.sin(np.pi*t/6)
exact_L = (5*12 + 3*(6/np.pi)*(1 - np.cos(2*np.pi))) * 3600  # sin term integrates to 0 over a full period
quad_val, quad_err = quad(Q, 0, 12)
print(f"Exact volume = {exact_L:,.0f} L | quad: {quad_val*3600:,.0f} L (error est {quad_err:.1e})")
exact_part = (5*4 + 3*(6/np.pi)*(1 - np.cos(np.pi*4/6))) * 3600   # exact volume over [0, 4] h
print(f"Exact volume over the first 4 h = {exact_part:,.1f} L")
print("(Over the full 12 h the sine term is a whole period, so even the trapezoid rule is exact - see note in docs.)")
for n in (3, 5, 9, 25, 101):
    t = np.linspace(0, 4, n); q = Q(t)
    trap = np.trapezoid(q, t)*3600; sim = simpson(q, x=t)*3600
    print(f"n={n:3d} points on [0,4]: trapezoid err {abs(trap-exact_part):10.3f} L | Simpson err {abs(sim-exact_part):10.6f} L")

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].plot(time_hours, power_kw, "o-"); ax[0].fill_between(time_hours, power_kw, alpha=0.25)
ax[0].set_xlabel("Time (h)"); ax[0].set_ylabel("Power (kW)"); ax[0].set_title(f"Area = energy ({energy_simpson:.2f} kWh)"); ax[0].grid(True)
ns = np.arange(3, 60, 2); et = [abs(np.trapezoid(Q(np.linspace(0,4,n)), np.linspace(0,4,n))*3600 - exact_part) for n in ns]
es = [abs(simpson(Q(np.linspace(0,4,n)), x=np.linspace(0,4,n))*3600 - exact_part) + 1e-12 for n in ns]
ax[1].semilogy(ns, et, label="Trapezoid"); ax[1].semilogy(ns, es, label="Simpson"); ax[1].set_xlabel("Number of sample points"); ax[1].set_ylabel("Absolute error (L)")
ax[1].set_title("Related case: error vs samples"); ax[1].legend(); ax[1].grid(True, which="both", alpha=0.4)
plt.tight_layout(); plt.savefig(os.path.join(FIG, "task16_integration.png"), dpi=130); plt.close()
