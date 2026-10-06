"""Task 15 - Numerical Differentiation
PART 1 original | PART 2 changed step size | PART 3 related case (acceleration from velocity)"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

def estimate_speed(time, position):
    speed = np.zeros_like(position)
    speed[0] = (position[1] - position[0]) / (time[1] - time[0])
    for i in range(1, len(time) - 1):
        speed[i] = (position[i + 1] - position[i - 1]) / (time[i + 1] - time[i - 1])
    speed[-1] = (position[-1] - position[-2]) / (time[-1] - time[-2])
    return speed

print("=== PART 1: Original - GPS speed ===")
time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
position = np.array([0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0])
speed = estimate_speed(time, position)
for t, x, v in zip(time, position, speed):
    print(f"t={t:.0f}s, position={x:.1f}m, estimated speed={v:.2f}m/s")
print("np.gradient check:", np.round(np.gradient(position, time), 2))
print("Worked example: (112-100)/2 =", (112-100)/2, "m/s")

print("\n=== PART 2: Changed input - step size h for f(x)=sin(x) at x=1 (exact cos(1)) ===")
exact = np.cos(1.0)
print(f"{'h':>8} {'forward err':>14} {'central err':>14}")
for h in (1.0, 0.1, 0.01, 0.001, 1e-6, 1e-10, 1e-14):
    fwd = (np.sin(1 + h) - np.sin(1)) / h
    cen = (np.sin(1 + h) - np.sin(1 - h)) / (2*h)
    print(f"{h:8.0e} {abs(fwd-exact):14.3e} {abs(cen-exact):14.3e}")
print("Changing GPS sample 4s position 22.7 -> 24.7 (a GPS glitch):")
pos2 = position.copy(); pos2[4] = 24.7
print("  speeds:", np.round(estimate_speed(time, pos2), 2))

print("\n=== PART 3: Related case - train acceleration from velocity data ===")
tt = np.arange(0, 11, 1.0)
vel = np.array([0.0, 1.9, 3.8, 5.4, 6.9, 8.1, 9.0, 9.6, 10.0, 10.2, 10.3])  # m/s
acc = np.gradient(vel, tt)
for t_, v_, a_ in zip(tt, vel, acc):
    print(f"t={t_:2.0f}s v={v_:5.1f} m/s a={a_:5.2f} m/s^2")
print(f"Peak acceleration: {acc.max():.2f} m/s^2 at t={tt[acc.argmax()]:.0f} s")
print(f"Second-order edges (edge_order=2) at t=0: {np.gradient(vel, tt, edge_order=2)[0]:.3f} vs first-order {acc[0]:.3f}")

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].plot(time, speed, "o-"); ax[0].set_xlabel("Time (s)"); ax[0].set_ylabel("Estimated speed (m/s)"); ax[0].set_title("Speed estimated from GPS position data"); ax[0].grid(True)
hs = np.logspace(-14, 0, 60)
ax[1].loglog(hs, np.abs((np.sin(1+hs)-np.sin(1))/hs - exact), label="Forward"); ax[1].loglog(hs, np.abs((np.sin(1+hs)-np.sin(1-hs))/(2*hs) - exact), label="Central")
ax[1].set_xlabel("Step size h"); ax[1].set_ylabel("Absolute error"); ax[1].set_title("Truncation vs round-off error"); ax[1].legend(); ax[1].grid(True, which="both", alpha=0.4)
plt.tight_layout(); plt.savefig(os.path.join(FIG, "task15_differentiation.png"), dpi=130); plt.close()
