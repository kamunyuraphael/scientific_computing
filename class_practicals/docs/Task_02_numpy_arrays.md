# Task 2 – NumPy Arrays and Numerical Computation

**Program:** `code/Task_02_numpy_arrays.py` · **Output:** `outputs/Task_02_numpy_arrays.txt`

---

## B. Input values and mathematical operation

| Item | Detail |
|---|---|
| Input | 24 hourly temperatures in °C (index 0 = 00:00 … index 23 = 23:00) |
| Operation 1 | Mean: x̄ = (Σ xᵢ) / n |
| Operation 2 | Minimum and maximum of the array |
| Operation 3 | Vectorized conversion F = 1.8·C + 32 applied to the whole array at once |

## C. Parameter change

**Change:** the midday (12:00) reading was changed from 29.4 °C to a faulty spike of 45.0 °C.

| Statistic | Original | After change |
|---|---|---|
| Mean | 23.12 °C | 23.77 °C |
| Maximum | 29.40 °C | 45.00 °C |
| Median | 22.75 °C | 22.75 °C |

**Explanation:** the mean rose by 15.6 / 24 = 0.65 °C because every value contributes to the sum. The maximum jumped by the full spike. The median did not move because it depends only on the middle ranking. One faulty sensor value distorts the mean and maximum but not the median.

## D. Meaning of the output

- Daily mean 23.12 °C: the typical temperature over the day.
- Minimum 17.50 °C (03:00) and maximum 29.40 °C (12:00): a daily range of about 11.9 °C.
- First six Fahrenheit values (65.3, 64.4, 64.04, 63.5, 64.22, 66.2 °F) show the early-morning cool period. The 1.8·C + 32 formula was applied to all 24 values in one expression, with no loop.

## E. Related real-world case: greenhouse IoT monitoring

**Assumptions:** hourly temperature follows a daily sine pattern around 24 °C (amplitude 6 °C, coolest around 03:00) plus random sensor noise N(0, 0.4²) (seed 7). Plants are stressed above 28 °C.

**Input data:** 24 simulated hourly readings, alert limit 28 °C.

**Output:**

| Quantity | Value |
|---|---|
| Mean / min / max | 23.84 °C / 17.64 °C / 30.28 °C |
| Hours above 28 °C | 6 (hours 12 to 17) |
| Standard deviation | 4.29 °C |
| Maximum in kelvin | 303.43 K |

**Interpretation:** a boolean mask (`greenhouse_c > 28`) finds the risky hours instantly. The greenhouse needs ventilation or shading from 12:00 to 17:00. Conversion to kelvin (`+ 273.15`) shows the same one-line vectorized pattern works for any unit change.
