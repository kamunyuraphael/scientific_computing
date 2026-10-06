"""Task 20 - Random Numbers and Monte Carlo Methods
PART 1 original | PART 2 changed capacity/N | PART 3 related case (project deadline risk + pi estimate)"""
import numpy as np
from scipy.stats import norm
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

print("=== PART 0: Estimate pi (7850 of 10000 -> 3.14 and a real run) ===")
rng = np.random.default_rng(42)
for n in (1_000, 100_000, 5_000_000):
    pts = rng.random((n, 2))
    inside = (pts**2).sum(axis=1) <= 1
    est = 4 * inside.mean()
    print(f"N={n:>9,}: pi ~ {est:.5f} | error {abs(est-np.pi):.5f}")

print("\n=== PART 1: Original - server overload ===")
rng = np.random.default_rng(42)
capacity, mean_demand, std_demand, N = 1000.0, 850.0, 120.0, 100_000
demand = rng.normal(mean_demand, std_demand, N)
overloaded = demand > capacity
overload_probability = overloaded.mean()
print(f"Estimated overload probability: {overload_probability:.4%}")
print(f"Number of overload cases: {overloaded.sum()} out of {N}")
exact = 1 - norm.cdf(capacity, mean_demand, std_demand)
se = np.sqrt(overload_probability*(1-overload_probability)/N)
print(f"Exact probability (normal CDF): {exact:.4%} | MC standard error: {se:.4%}")
print(f"95% interval: [{overload_probability-1.96*se:.4%}, {overload_probability+1.96*se:.4%}]")
running_probability = np.cumsum(overloaded) / np.arange(1, N + 1)

print("\n=== PART 2: Changed input - capacity 1000 -> 1150 (rare event), and N = 1,000 ===")
for cap in (900, 1000, 1150):
    for n in (1_000, 100_000):
        d = np.random.default_rng(1).normal(850, 120, n)
        p_ = (d > cap).mean()
        print(f"capacity {cap}, N={n:>7,}: estimate {p_:.4%} | exact {1-norm.cdf(cap, 850, 120):.4%}")
print("Std demand 120 -> 200 at capacity 1000:", f"{(np.random.default_rng(1).normal(850, 200, 100_000) > 1000).mean():.4%}",
      f"(exact {1-norm.cdf(1000, 850, 200):.4%})")

print("\n=== PART 3: Related case - will a 3-task project finish within 30 days? ===")
rng = np.random.default_rng(2026)
M = 200_000
# triangular(min, most likely, max) in days; tasks run in sequence
design = rng.triangular(5, 8, 14, M)
build = rng.triangular(10, 14, 24, M)
test = rng.triangular(4, 6, 12, M)
total = design + build + test
deadline = 30.0
print(f"Mean total duration: {total.mean():.2f} days | std {total.std():.2f}")
print(f"P(total > {deadline:.0f} days) = {(total > deadline).mean():.4%}")
print(f"Median {np.median(total):.2f} | 90th percentile {np.percentile(total, 90):.2f} | 95th percentile {np.percentile(total, 95):.2f} days")
print(f"Sum of 'most likely' values = {8+14+6} days (ignores skew; mean is {total.mean():.2f})")
for dl in (26, 28, 30, 32, 35):
    print(f"  deadline {dl} days -> P(late) = {(total > dl).mean():.2%}")

idx = np.unique(np.logspace(1, np.log10(N), 200).astype(int)) - 1
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].semilogx(idx + 1, running_probability[idx], label="Running estimate"); ax[0].axhline(exact, ls="--", c="r", label=f"Exact {exact:.3%}")
ax[0].set_xlabel("Number of simulations"); ax[0].set_ylabel("Estimated overload probability"); ax[0].set_title("Monte Carlo estimate of server-overload risk"); ax[0].legend(); ax[0].grid(True)
ax[1].hist(total, bins=60, density=True, alpha=0.7); ax[1].axvline(deadline, c="r", ls="--", label=f"Deadline {deadline:.0f} d")
ax[1].set_xlabel("Total project duration (days)"); ax[1].set_ylabel("Density"); ax[1].set_title("Related case: project duration risk"); ax[1].legend(); ax[1].grid(True)
plt.tight_layout(); plt.savefig(os.path.join(FIG, "task20_monte_carlo.png"), dpi=130); plt.close()
