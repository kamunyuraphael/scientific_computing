# Task 15 – Numerical Differentiation

**Program:** `code/Task_15_numerical_differentiation.py` · **Figure:** `figures/task15_differentiation.png`

---

## B. Input values and mathematical operation

| Item | Detail |
|---|---|
| Data | Time 0 to 6 s; GPS position 0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0 m |
| First point | Forward difference (x₁ − x₀)/Δt |
| Interior points | Central difference (xᵢ₊₁ − xᵢ₋₁)/(2Δt) |
| Last point | Backward difference (x₆ − x₅)/Δt |

**Estimated speed (m/s):** 4.80, 5.10, 5.65, 6.25, 6.95, 7.65, 8.00 (identical to `np.gradient`). Worked example: (112 − 100)/2 = 6 m/s.

## C. Parameter change

**Change 1: step size h** for f(x) = sin x at x = 1, exact derivative cos 1:

| h | Forward error | Central error |
|---|---|---|
| 1 | 4.7 × 10⁻¹ | 8.6 × 10⁻² |
| 0.1 | 4.3 × 10⁻² | 9.0 × 10⁻⁴ |
| 0.01 | 4.2 × 10⁻³ | 9.0 × 10⁻⁶ |
| 10⁻⁶ | 4.2 × 10⁻⁷ | 2.8 × 10⁻¹¹ |
| 10⁻¹⁰ | 5.8 × 10⁻⁸ | 5.8 × 10⁻⁸ |
| 10⁻¹⁴ | 3.7 × 10⁻³ | 3.7 × 10⁻³ |

**Change 2: a GPS glitch**, position at 4 s changed 22.7 → 24.7 m. Speeds become 4.80, 5.10, 5.65, **7.25**, 6.95, **6.65**, 8.00. Only the neighbouring points (3 s and 5 s) are changed.

**Explanation:** forward error falls 10× per 10× smaller h (first order); central error falls 100× (second order). Below about h = 10⁻⁸ round-off error takes over and the error rises again. A single bad position value spoils the speed estimates at its two neighbours.

## D. Meaning of the output and graph

- The vehicle accelerates steadily from 4.8 m/s to 8.0 m/s over 6 s (about 0.5 m/s²).
- **Graph (right):** a log-log plot with a V shape. Decreasing h helps until truncation error meets round-off error, so the best step size is not the smallest one.

## E. Related real-world case: acceleration of a train from velocity data

**Assumptions:** velocity recorded every second for 10 s (m/s): 0, 1.9, 3.8, 5.4, 6.9, 8.1, 9.0, 9.6, 10.0, 10.2, 10.3. Acceleration a = dv/dt estimated with `np.gradient`.

**Output:** acceleration falls from 1.90 m/s² (t = 0 to 1 s) to 1.55 at 3 s, 0.75 at 6 s, and 0.10 m/s² at 10 s.

**Interpretation:** the train accelerates hard at departure, then the push fades as it nears a cruising speed of about 10.3 m/s. Peak acceleration (1.9 m/s²) occurs at the start, which matters for passenger comfort limits.
