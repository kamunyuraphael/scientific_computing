"""Task 17 - ODEs: Euler Method
PART 1 original | PART 2 changed step size / k | PART 3 related case (logistic population growth)"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

def euler(f, y0, t0, t_end, h):
    t = np.arange(t0, t_end + h/2, h); y = np.zeros_like(t); y[0] = y0
    for i in range(len(t) - 1):
        y[i + 1] = y[i] + h * f(t[i], y[i])
    return t, y

print("=== PART 0: Worked example dy/dt = y, y(0)=1, h=0.1 ===")
t, y = euler(lambda t, y: y, 1.0, 0, 0.2, 0.1)
print("y1, y2 =", np.round(y[1:], 4), "(exact e^0.1, e^0.2 =", round(np.exp(0.1), 4), round(np.exp(0.2), 4), ")")

T_ambient, T_initial = 25.0, 90.0
def cooling(k):
    return lambda t, T: -k * (T - T_ambient)
exact_fn = lambda t, k: T_ambient + (T_initial - T_ambient) * np.exp(-k * t)

print("\n=== PART 1: Original - cooling, k=0.12, h=1 min, 30 min ===")
time, temperature = euler(cooling(0.12), T_initial, 0, 30, 1.0)
exact = exact_fn(time, 0.12)
print(f"Euler temperature after 30 min: {temperature[-1]:.2f} C")
print(f"Exact temperature after 30 min: {exact[-1]:.2f} C")
print(f"Final absolute error: {abs(temperature[-1]-exact[-1]):.4f} C")

print("\n=== PART 2: Changed input - step size h and rate k ===")
for h in (5.0, 2.0, 1.0, 0.5, 0.1, 0.01):
    t_, y_ = euler(cooling(0.12), T_initial, 0, 30, h)
    print(f"h={h:5.2f} min: T(30)={y_[-1]:.4f} C | error {abs(y_[-1]-exact_fn(30, 0.12)):.5f} C")
t_, y_ = euler(cooling(0.12), T_initial, 0, 30, 20.0)
print("h=20 (h*k=2.4 > 2): oscillating/unstable ->", np.round(y_, 2))
t_, y_ = euler(cooling(0.30), T_initial, 0, 30, 1.0)
print(f"k=0.30 (faster cooling), h=1: T(30)={y_[-1]:.3f} C vs exact {exact_fn(30, 0.30):.3f} C")

print("\n=== PART 3: Related case - logistic growth of a fish population (r=0.4/yr, K=1000, P0=50) ===")
r, K, P0 = 0.4, 1000.0, 50.0
logistic = lambda t, P: r * P * (1 - P / K)
exact_log = lambda t: K / (1 + (K - P0)/P0 * np.exp(-r * t))
for h in (2.0, 1.0, 0.25):
    t_, P_ = euler(logistic, P0, 0, 30, h)
    print(f"h={h:4.2f} yr: P(10)={P_[int(round(10/h))]:8.2f} | P(30)={P_[-1]:8.2f} | error at t=10: {abs(P_[int(round(10/h))]-exact_log(10)):8.3f}")
print(f"Exact: P(10)={exact_log(10):.2f}, P(30)={exact_log(30):.2f} -> approaches carrying capacity K={K:.0f}")
t_half = np.log((K - P0)/P0)/r
print(f"Population reaches K/2=500 at t = {t_half:.2f} years (inflection point of the S-curve)")

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].plot(time, temperature, "o", ms=4, label="Euler (h=1)"); ax[0].plot(time, exact, label="Exact")
t5, y5 = euler(cooling(0.12), T_initial, 0, 30, 5.0); ax[0].plot(t5, y5, "s--", ms=4, label="Euler (h=5)")
ax[0].set_xlabel("Time (minutes)"); ax[0].set_ylabel("Temperature (C)"); ax[0].set_title("Cooling of a hot object"); ax[0].legend(); ax[0].grid(True)
tt = np.linspace(0, 30, 300); ax[1].plot(tt, exact_log(tt), label="Exact")
for h in (2.0, 0.25):
    t_, P_ = euler(logistic, P0, 0, 30, h); ax[1].plot(t_, P_, "o--", ms=3, label=f"Euler h={h}")
ax[1].axhline(K, ls=":", c="grey"); ax[1].set_xlabel("Years"); ax[1].set_ylabel("Population"); ax[1].set_title("Related case: logistic growth"); ax[1].legend(); ax[1].grid(True)
plt.tight_layout(); plt.savefig(os.path.join(FIG, "task17_euler.png"), dpi=130); plt.close()
