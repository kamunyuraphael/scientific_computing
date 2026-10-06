# Task 18 – Numerical Solution of ODEs Using SciPy

**Program:** `code/Task_18_scipy_ode.py` · **Figure:** `figures/task18_ode.png`

---

## B. Input values and mathematical operation

| Item | Detail |
|---|---|
| ODE | RC circuit: dV/dt = (Vs − V)/(R·C) |
| Inputs | Vs = 5 V, R = 1000 Ω, C = 0.001 F (so τ = RC = 1 s), V₀ = 0 V, time 0 to 5 s |
| Solver | `solve_ivp` (default RK45, adaptive step) with rtol 10⁻⁹, atol 10⁻¹¹ |
| Validation | Exact V(t) = 5·(1 − e^(−t/RC)) |

**Results:** V(5 s) = 4.9663 V; maximum error versus exact = 9.3 × 10⁻¹⁰ V; 386 function evaluations. At t = τ = 1 s, V = 3.1605 V, which is 63.2 % of the supply (theory 3.1606 V).

## C. Parameter change

| Change | Result |
|---|---|
| C = 0.004 F (τ = 4 s) | V(5 s) = 3.5675 V (71.3 % of supply) |
| Looser tolerance rtol 10⁻³ | max error 6.6 × 10⁻⁴ V with only 56 evaluations (was 386) |
| Radau solver (for stiff problems) | max error 4.9 × 10⁻¹⁰ V, 1435 evaluations |

**Explanation:** a bigger capacitor charges more slowly because the time constant is larger. The tolerance controls the accuracy-versus-cost trade-off. Radau is more expensive here but is the right choice for stiff systems.

## D. Meaning of the output and graph

- After one time constant the capacitor reaches 63 % of the supply voltage. After five time constants it is essentially full (4.97 V).
- **Graph (left):** the solver curve and the dashed exact curve overlap, so the numerical error is invisible. The slower curve for C = 4 mF rises more gradually.

## E. Related real-world case: SIR epidemic model

**Assumptions:** population 10,000 with 10 initially infected. Infection rate β = 0.35 per day and recovery rate γ = 0.10 per day, so R₀ = β/γ = 3.5. The model: dS/dt = −βSI/N, dI/dt = βSI/N − γI, dR/dt = γI.

| Scenario | Peak infected | Peak day | Total infected |
|---|---|---|---|
| No control (β = 0.35) | 3566 | 31.8 | 9660 (96.6 %) |
| Distancing (β = 0.18, R₀ = 1.8) | 1185 | 80.4 | 7223 (72.2 %) |

The check S + I + R = N holds to 7 × 10⁻¹².

**Interpretation:** reducing contact halves R₀, cutting the peak to about one third and delaying it by seven weeks. That relieves pressure on hospitals even though many people are still infected in the end. The right-hand graph shows the infection curve (dashed black for distancing) as a lower, later, wider hump.
