# Task 14 – Curve Fitting and Approximation

**Program:** `code/Task_14_curve_fitting.py` · **Figure:** `figures/task14_curve_fit.png`

---

## B. Input values and mathematical operation

| Item | Detail |
|---|---|
| Data | Users 50, 100, …, 350 and response times 82, 95, 115, 145, 185, 238, 305 ms |
| Model | y = a·x² + b·x + c |
| Operation | `curve_fit` chooses a, b, c to minimize Σ(yᵢ − ŷᵢ)², the sum of squared residuals |

**Results:** y = 0.002167·x² − 0.1345·x + 85.00; RMSE = 1.55 ms; prediction at 400 users = 377.86 ms. Residuals are small (largest about ±1.8 ms) with mixed signs and no steadily growing trend, which suggests the model has no strong systematic bias.

## C. Parameter change (different model)

| Model | RMSE | Prediction at 400 users |
|---|---|---|
| Quadratic (original) | 1.55 ms | 377.9 ms |
| Straight line: y = 0.7321x + 20.00 | 18.83 ms | 312.9 ms |
| Exponential: y = 33.65·e^(0.00596x) + 34.72 | 1.43 ms | 400.4 ms |
| Cubic polynomial (4 parameters, 7 points) | 0.14 ms | (overfits) |

**Explanation:** the line is a poor fit because delay accelerates. The quadratic and exponential fit the data equally well but disagree by about 22 ms outside the data (400 users). Good in-range fit does not guarantee a good prediction beyond the data. The cubic fits almost perfectly but is memorising noise, not modelling the system.

## D. Meaning of the output and graph

- The positive x² coefficient means each extra user adds more delay than the previous one: congestion.
- **Graph (left):** the quadratic curve passes close to all points. The dashed straight line drifts away at both ends, showing the line is inadequate.

## E. Related real-world case: logistic growth of app users

**Assumptions:** weekly active users follow logistic growth y = K / (1 + e^(−r(t − t₀))) with true K = 5000, r = 0.45, t₀ = 9, plus noise (standard deviation 90, seed 3), over 21 weeks.

**Output:**

| Parameter | True | Fitted | Standard error |
|---|---|---|---|
| K (capacity) | 5000 | 4971.2 | 58.0 |
| r (growth rate) | 0.45 | 0.464 | 0.020 |
| t₀ (midpoint week) | 9 | 8.97 | 0.11 |

RMSE = 107.2 users, R² = 0.9969, predicted users in week 25 = 4968.

**Interpretation:** the market saturates near 5000 users and the fastest growth happens around week 9. If only weeks 0 to 8 are used, the fit gives K = 6111 (22 % too high), a warning that forecasts made before the curve flattens are unreliable. The right-hand graph shows the S-curve levelling off at K (dotted line).
