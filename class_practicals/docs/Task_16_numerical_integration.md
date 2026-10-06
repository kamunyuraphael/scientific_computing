# Task 16 – Numerical Integration

**Program:** `code/Task_16_numerical_integration.py` · **Figure:** `figures/task16_integration.png`

---

## B. Input values and mathematical operation

| Item | Detail |
|---|---|
| Data | Smart-meter power (kW) every 2 h from 0 to 12 h: 0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9 |
| Quantity | Energy E = ∫ P dt (kWh) |
| Trapezoid | Sum of trapezoid areas: ∑ h(Pᵢ + Pᵢ₊₁)/2 |
| Simpson | Uses parabolas through three points (weights 1, 4, 2, 4, …, 1 times h/3) |

**Results:** trapezoid 15.700 kWh, Simpson 15.800 kWh, difference 0.100 kWh. Check: constant 2 kW for 3 h gives 6 kWh.

## C. Parameter change

| Change | Trapezoid | Simpson |
|---|---|---|
| Original (2 h readings) | 15.700 | 15.800 |
| Readings only every 4 h | 15.400 | 15.967 |
| 6 h reading changed 1.8 → 3.0 kW | 18.100 | 19.000 |

**Explanation:** fewer samples make the two methods disagree more. A spike raises the answer by weight × change: trapezoid weight at an interior point is h = 2, so +1.2 × 2 = +2.4; Simpson weight at that point is 4h/3 = 2.67, so +1.2 × 2.67 = +3.2 kWh.

## D. Meaning of the output and graph

- The day's energy use is about 15.8 kWh (the area under the power curve).
- **Graph (left):** the shaded region under the power curve is the energy. Usage peaks (1.8 kW) at 6 h.

## E. Related real-world case: total water volume from flow-rate data

**Assumptions:** inflow Q(t) = 5 + 3·sin(πt/6) litres per second, t in hours. The exact volume is known, so errors can be measured.

- Full 12 h: exact volume = 216,000 L (matches SciPy `quad`). The sine part covers a whole period and cancels, so even the trapezoid rule is exact here.
- First 4 h only (exact volume 102,939.7 L), so errors are visible:

| Sample points | Trapezoid error (L) | Simpson error (L) |
|---|---|---|
| 3 | 2880.5 | 237.2 |
| 5 | 710.1 | 13.35 |
| 9 | 176.9 | 0.81 |
| 25 | 19.6 | 0.0100 |
| 101 | 1.13 | 0.000033 |

**Interpretation:** doubling the points cuts the trapezoid error by about 4× (error ∝ h²) and the Simpson error by about 16× (error ∝ h⁴). The right-hand graph shows two straight lines on a log scale, Simpson much lower. Simpson is the better choice for smooth data.
