"""Task 14 - Curve Fitting and Approximation
PART 1 original | PART 2 changed model | PART 3 related case (logistic growth of app users)"""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
response_ms = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)
def model(x, a, b, c): return a*x**2 + b*x + c
rmse = lambda y, p: float(np.sqrt(np.mean((y - p)**2)))

print("=== PART 1: Original - quadratic ===")
parameters, covariance = curve_fit(model, users, response_ms)
a, b, c = parameters
predicted = model(users, a, b, c)
print(f"Fitted model: y = {a:.6f}x^2 + {b:.4f}x + {c:.2f}")
print(f"RMSE: {rmse(response_ms, predicted):.2f} ms")
print(f"Predicted response at 400 users: {model(400, a, b, c):.2f} ms")
print("Residuals:", np.round(response_ms - predicted, 2))
print("Parameter standard errors:", np.round(np.sqrt(np.diag(covariance)), 6))

print("\n=== PART 2: Changed model - straight line and exponential ===")
lin = np.polyfit(users, response_ms, 1)
print(f"Linear: y = {lin[0]:.4f}x + {lin[1]:.2f} | RMSE {rmse(response_ms, np.polyval(lin, users)):.2f} | at 400: {np.polyval(lin, 400):.1f} ms")
def expo(x, a, b, c): return a*np.exp(b*x) + c
pe, _ = curve_fit(expo, users, response_ms, p0=[10, 0.01, 70], maxfev=20000)
print(f"Exponential: y = {pe[0]:.3f}*exp({pe[1]:.5f}x) + {pe[2]:.2f} | RMSE {rmse(response_ms, expo(users, *pe)):.2f} | at 400: {expo(400, *pe):.1f} ms")
print("Order-3 polynomial RMSE:", round(rmse(response_ms, np.polyval(np.polyfit(users, response_ms, 3), users)), 3), "(overfits 7 points with 4 parameters)")

print("\n=== PART 3: Related case - logistic growth of app users (synthetic noisy data) ===")
rng = np.random.default_rng(3)
weeks = np.arange(0, 21, dtype=float)
def logistic(t, K, r, t0): return K / (1 + np.exp(-r*(t - t0)))
true = (5000, 0.45, 9)
obs = logistic(weeks, *true) + rng.normal(0, 90, weeks.size)
p, cov = curve_fit(logistic, weeks, obs, p0=[4000, 0.3, 8])
print(f"True   K={true[0]}, r={true[1]}, t0={true[2]}")
print(f"Fitted K={p[0]:.1f}, r={p[1]:.3f}, t0={p[2]:.2f} | RMSE {rmse(obs, logistic(weeks, *p)):.1f} users")
print("Std errors:", np.round(np.sqrt(np.diag(cov)), 3))
print(f"Predicted users in week 25: {logistic(25, *p):.0f} | carrying capacity K ~ {p[0]:.0f}")
ss_res = np.sum((obs - logistic(weeks, *p))**2); ss_tot = np.sum((obs - obs.mean())**2)
print(f"R^2 = {1 - ss_res/ss_tot:.4f}")
# fitting only early weeks: how well is K recovered?
early = weeks <= 8
pe2, _ = curve_fit(logistic, weeks[early], obs[early], p0=[4000, 0.3, 8], maxfev=20000)
print(f"Fit using only weeks 0-8: K={pe2[0]:.0f} (true 5000) -> extrapolation is unreliable")

x_plot = np.linspace(users.min(), 400, 300)
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].scatter(users, response_ms, label="Measurements"); ax[0].plot(x_plot, model(x_plot, a, b, c), label="Quadratic fit")
ax[0].plot(x_plot, np.polyval(lin, x_plot), "--", label="Linear fit")
ax[0].set_xlabel("Concurrent users"); ax[0].set_ylabel("Response time (ms)"); ax[0].set_title("Server response-time curve fitting"); ax[0].legend(); ax[0].grid(True)
w = np.linspace(0, 25, 300)
ax[1].scatter(weeks, obs, s=14, label="Observed"); ax[1].plot(w, logistic(w, *p), label="Logistic fit")
ax[1].axhline(p[0], ls=":", c="grey"); ax[1].set_xlabel("Week"); ax[1].set_ylabel("Active users"); ax[1].set_title("Related case: logistic growth"); ax[1].legend(); ax[1].grid(True)
plt.tight_layout(); plt.savefig(os.path.join(FIG, "task14_curve_fit.png"), dpi=130); plt.close()
