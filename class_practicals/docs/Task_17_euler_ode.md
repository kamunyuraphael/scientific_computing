# Task 17 – Ordinary Differential Equations: Euler Method

**Program:** `code/Task_17_euler_ode.py` · **Figure:** `figures/task17_euler.png`

---

## B. Input values and mathematical operation

| Item | Detail |
|---|---|
| ODE | Newton's law of cooling: dT/dt = −k(T − T_ambient) |
| Inputs | T_ambient = 25 °C, T₀ = 90 °C, k = 0.12 per minute, step h = 1 min, end time 30 min |
| Euler update | Tₙ₊₁ = Tₙ + h·(−k(Tₙ − 25)) |
| Validation | Exact solution T(t) = 25 + 65·e^(−0.12t) |

**Results:** Euler T(30) = 26.40 °C; exact = 26.78 °C; error = 0.372 °C. Worked example dy/dt = y, h = 0.1: Euler gives 1.1 and 1.21 (exact 1.1052 and 1.2214).

## C. Parameter change

**Change 1: step size** (k = 0.12, exact T(30) = 26.7760 °C)

| h (min) | Euler T(30) | Error |
|---|---|---|
| 5 | 25.266 | 1.510 |
| 2 | 26.060 | 0.717 |
| 1 | 26.404 | 0.372 |
| 0.5 | 26.587 | 0.189 |
| 0.1 | 26.738 | 0.0383 |
| 0.01 | 26.772 | 0.0038 |

**Change 2:** h = 20 min makes h·k = 2.4, giving 90 → −66 °C (below the ambient 25 °C, physically impossible, so Euler is unstable). With k = 0.30 and h = 1, T(30) = 25.001 °C against exact 25.008 °C.

**Explanation:** the error falls in proportion to h (Euler is first order): 10× smaller step, 10× smaller error. If h·k > 2 the method becomes unstable and the answer is wrong.

## D. Meaning of the output and graph

- The object cools quickly at first and then slowly approaches room temperature (25 °C), because the cooling rate is proportional to the temperature difference.
- **Graph (left):** the h = 1 Euler points sit just below the exact curve. The coarse h = 5 line is visibly lower, showing that Euler cools too fast when steps are large.

## E. Related real-world case: logistic growth of a fish population

**Assumptions:** dP/dt = r·P·(1 − P/K) with growth rate r = 0.4 per year, carrying capacity K = 1000 and initial population 50. Exact solution available for validation.

| Step h | Euler P(10) | Error at 10 years |
|---|---|---|
| 2.0 | 600.75 | 141.1 |
| 1.0 | 679.03 | 62.8 |
| 0.25 | 727.91 | 13.9 |
| Exact | 741.84 | 0 |

All runs approach K = 1000 by year 30 (exact 999.88). The population passes 500 (half the capacity, the fastest-growth point) at 7.36 years.

**Interpretation:** growth is slow when the population is small, fastest at half capacity, and slows again near the limit (S-shaped curve). Euler lags behind the true curve, and small steps are needed where the curve is steepest.
