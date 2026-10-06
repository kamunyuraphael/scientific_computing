# Task 13 – Interpolation

**Program:** `code/Task_13_interpolation.py` · **Figure:** `figures/task13_interpolation.png`

---

## B. Input values and mathematical operation

| Item | Detail |
|---|---|
| Data | Hours 8 to 14 and temperatures 18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0 °C |
| Linear | `interp1d(kind="linear")`: straight line between neighbours |
| Cubic spline | `CubicSpline`: cubic pieces joined smoothly (continuous first and second derivatives) |
| Evaluation | 37 times, one every 10 minutes (1/6 hour) |

**Results at 10:30:** linear 23.25 °C, cubic 23.36 °C. Worked example check: 20 °C at 10:00 and 24 °C at 12:00 gives 22.0 °C at 11:00.

## C. Parameter change

| Change | Result |
|---|---|
| Quadratic interpolation | 23.36 °C at 10:30 (about the same as cubic) |
| 10:00 reading changed 22.5 → 26.5 (faulty) | Linear 25.25 °C, cubic 25.68 °C at 10:30 |
| Ask for 15:00 (outside 8 to 14) | `ValueError`: extrapolation not allowed |

**Explanation:** the estimate at 10:30 is pulled up by the bad reading in both methods. The cubic spline also overshoots (maximum 26.57 °C against a data maximum of 26.5 °C), because smooth curves can swing past data. Interpolation is only valid inside the measured range.

## D. Meaning of the output and graph

- **Graph (left):** dots are measurements. The linear estimate is a polyline with corners at each hour. The cubic spline is a smooth curve that bends gradually, so it follows real temperature change more naturally.
- Both curves pass exactly through every measured point, which is the defining property of interpolation (unlike curve fitting in Task 14).

## E. Related real-world case: filling gaps in an air-quality (PM2.5) sensor

**Assumptions:** a sensor should record PM2.5 each hour for 24 hours, following a smooth daily pattern, but readings at hours 5, 6, 7, 14 and 15 are missing. The true values are known (simulated), so the error can be measured.

| Hour | True | Linear | Cubic |
|---|---|---|---|
| 5 | 48.66 | 52.32 | 50.16 |
| 6 | 47.00 | 52.32 | 49.43 |
| 7 | 48.66 | 52.32 | 50.16 |
| 14 | 17.00 | 22.00 | 17.75 |
| 15 | 15.20 | 19.84 | 15.91 |
| **RMSE** | | **4.51** | **1.51** |

**Interpretation:** the cubic spline is about three times more accurate on this smooth signal. Linear interpolation across the 4-hour gap draws a flat line and misses the dip, as the right-hand graph shows. For fast, jagged signals linear interpolation can be safer.
