"""Task 13 - Interpolation
PART 1 original | PART 2 changed method/data | PART 3 related case (air-quality gap with known truth)"""
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

print("=== PART 1: Original ===")
hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temperature = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])
linear = interp1d(hours, temperature, kind="linear"); cubic = CubicSpline(hours, temperature)
ten_minute_times = np.arange(8, 14 + 1/6, 1/6)
linear_estimates, cubic_estimates = linear(ten_minute_times), cubic(ten_minute_times)
print(f"Linear estimate at 10:30: {float(linear(10.5)):.2f} C")
print(f"Cubic estimate at 10:30: {float(cubic(10.5)):.2f} C")
print("Number of 10-minute estimates:", len(ten_minute_times))
print(f"Worked example check: 20C at 10:00, 24C at 12:00 -> {float(interp1d([10,12],[20,24])(11)):.1f} C at 11:00")

print("\n=== PART 2: Changed input - quadratic interp, then change the 10:00 reading 22.5 -> 26.5 ===")
quad = interp1d(hours, temperature, kind="quadratic")
print(f"Quadratic at 10:30: {float(quad(10.5)):.3f} C")
t2 = temperature.copy(); t2[2] = 26.5
print(f"Linear at 10:30 with new reading: {float(interp1d(hours, t2)(10.5)):.3f} C | cubic: {float(CubicSpline(hours, t2)(10.5)):.3f} C")
print("Cubic spline overshoot with bad reading, max between 9 and 11:", round(float(CubicSpline(hours, t2)(np.linspace(9, 11, 200)).max()), 3))
try:
    linear(15.0)
except ValueError as e:
    print("Extrapolation at 15:00 raises ValueError ->", str(e)[:60])

print("\n=== PART 3: Related case - PM2.5 sensor with missing readings, scored against truth ===")
t_full = np.arange(0, 25, 1.0)
true_pm = 35 + 20*np.sin(2*np.pi*t_full/24) + 8*np.sin(2*np.pi*t_full/8)
missing = np.array([5, 6, 7, 14, 15])
keep = np.setdiff1d(np.arange(len(t_full)), missing)
lin = interp1d(t_full[keep], true_pm[keep])(t_full[missing])
cub = CubicSpline(t_full[keep], true_pm[keep])(t_full[missing])
print("Missing hours:", t_full[missing])
print("True   :", np.round(true_pm[missing], 2))
print("Linear :", np.round(lin, 2), "| RMSE", round(float(np.sqrt(np.mean((lin - true_pm[missing])**2))), 3))
print("Cubic  :", np.round(cub, 2), "| RMSE", round(float(np.sqrt(np.mean((cub - true_pm[missing])**2))), 3))

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].scatter(hours, temperature, label="Hourly measurements", zorder=5)
ax[0].plot(ten_minute_times, linear_estimates, label="Linear"); ax[0].plot(ten_minute_times, cubic_estimates, label="Cubic spline")
ax[0].set_xlabel("Hour of day"); ax[0].set_ylabel("Temperature (C)"); ax[0].set_title("Temperature interpolation"); ax[0].legend(); ax[0].grid(True)
tt = np.linspace(0, 24, 400)
ax[1].plot(tt, 35 + 20*np.sin(2*np.pi*tt/24) + 8*np.sin(2*np.pi*tt/8), c="grey", label="True curve")
ax[1].scatter(t_full[keep], true_pm[keep], s=12, label="Recorded"); ax[1].scatter(t_full[missing], lin, marker="x", c="r", label="Linear fill")
ax[1].scatter(t_full[missing], cub, marker="+", c="g", s=60, label="Cubic fill")
ax[1].set_xlabel("Hour"); ax[1].set_ylabel("PM2.5 (ug/m3)"); ax[1].set_title("Related case: filling sensor gaps"); ax[1].legend(fontsize=8); ax[1].grid(True)
plt.tight_layout(); plt.savefig(os.path.join(FIG, "task13_interpolation.png"), dpi=130); plt.close()
