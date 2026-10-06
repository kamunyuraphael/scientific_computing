"""Task 18 - Numerical Solution of ODEs Using SciPy
PART 1 original | PART 2 changed R*C and tolerance | PART 3 related case (SIR epidemic model)"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

def rc_solve(R, C, Vs=5.0, V0=0.0, t_end=5.0, rtol=1e-9, atol=1e-11, method="RK45"):
    f = lambda t, V: [(Vs - V[0]) / (R * C)]
    t_eval = np.linspace(0, t_end, 200)
    sol = solve_ivp(f, (0, t_end), [V0], t_eval=t_eval, rtol=rtol, atol=atol, method=method)
    exact = Vs * (1 - np.exp(-sol.t / (R * C))) + V0*np.exp(-sol.t/(R*C))
    return sol, exact

print("=== PART 1: Original - RC charging, R=1000, C=0.001 (tau = 1 s) ===")
solution, exact = rc_solve(1000.0, 0.001)
print("Solver success:", solution.success)
print(f"Capacitor voltage at 5 s: {solution.y[0, -1]:.4f} V")
print(f"Maximum error against exact solution: {np.max(np.abs(solution.y[0]-exact)):.3e} V")
print("Function evaluations:", solution.nfev)
print(f"Voltage at t = tau (1 s): {np.interp(1.0, solution.t, solution.y[0]):.4f} V (theory 63.2% of 5 V = {5*(1-np.exp(-1)):.4f})")

print("\n=== PART 2: Changed input - C 0.001 -> 0.004 (tau = 4 s); then looser tolerance; then Radau solver ===")
s2, e2 = rc_solve(1000.0, 0.004)
print(f"V(5 s) = {s2.y[0,-1]:.4f} V (theory {5*(1-np.exp(-5/4)):.4f}); fraction of supply reached {s2.y[0,-1]/5:.1%}")
s3, e3 = rc_solve(1000.0, 0.001, rtol=1e-3, atol=1e-6)
print(f"Loose tolerance rtol=1e-3: max error {np.max(np.abs(s3.y[0]-e3)):.2e} V, nfev {s3.nfev} (was {solution.nfev})")
s4, e4 = rc_solve(1000.0, 0.001, method="Radau")
print(f"Stiff-capable solver Radau: max error {np.max(np.abs(s4.y[0]-e4)):.2e} V, nfev {s4.nfev}")

print("\n=== PART 3: Related case - SIR epidemic, population 10,000, beta=0.35, gamma=0.10 ===")
N, beta, gamma = 10_000.0, 0.35, 0.10
def sir(t, y, beta=beta):
    S, I, R = y
    return [-beta*S*I/N, beta*S*I/N - gamma*I, gamma*I]
t_eval = np.linspace(0, 160, 801)
s = solve_ivp(sir, (0, 160), [N-10, 10, 0], t_eval=t_eval, rtol=1e-8, atol=1e-10)
S, I, R = s.y
print(f"R0 = beta/gamma = {beta/gamma:.2f}")
print(f"Peak infections: {I.max():.0f} on day {s.t[I.argmax()]:.1f}")
print(f"Total ever infected (final R): {R[-1]:.0f} ({R[-1]/N:.1%}) | still susceptible: {S[-1]:.0f}")
print(f"Conservation check max |S+I+R-N|: {np.max(np.abs(S+I+R-N)):.2e}")
s_lock = solve_ivp(lambda t, y: sir(t, y, beta=0.18), (0, 160), [N-10, 10, 0], t_eval=t_eval, rtol=1e-8, atol=1e-10)
print(f"With distancing beta=0.18 (R0={0.18/gamma:.1f}): peak {s_lock.y[1].max():.0f} on day {s_lock.t[s_lock.y[1].argmax()]:.1f}; final infected {s_lock.y[2,-1]:.0f} ({s_lock.y[2,-1]/N:.1%})")

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].plot(solution.t, solution.y[0], label="solve_ivp"); ax[0].plot(solution.t, exact, "--", label="Exact")
ax[0].plot(s2.t, s2.y[0], label="C = 4 mF (tau = 4 s)"); ax[0].set_xlabel("Time (s)"); ax[0].set_ylabel("Capacitor voltage (V)")
ax[0].set_title("RC circuit charging"); ax[0].legend(); ax[0].grid(True)
ax[1].plot(s.t, S, label="Susceptible"); ax[1].plot(s.t, I, label="Infected"); ax[1].plot(s.t, R, label="Recovered")
ax[1].plot(s_lock.t, s_lock.y[1], "k--", label="Infected (distancing)")
ax[1].set_xlabel("Day"); ax[1].set_ylabel("People"); ax[1].set_title("Related case: SIR epidemic"); ax[1].legend(fontsize=8); ax[1].grid(True)
plt.tight_layout(); plt.savefig(os.path.join(FIG, "task18_ode.png"), dpi=130); plt.close()
