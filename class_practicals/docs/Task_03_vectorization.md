# Task 3 – Mathematical Functions and Vectorization

**Program:** `code/Task_03_vectorization.py` · **Output:** `outputs/Task_03_vectorization.txt`

> Timing values depend on the computer and change slightly on every run. The ratios (speed-ups) are what matter.

---

## B. Input values and mathematical operation

| Item | Detail |
|---|---|
| Input | 1,000,000 simulated latency readings, uniform between 5 and 250 ms (seed 42) |
| Operation | Convert ms → s (divide by 1000), then square: y = (x / 1000)² |
| Two versions | A Python `for` loop versus one NumPy expression |
| Measurement | `timeit` runs both and compares execution time |

## C. Parameter change

**Change:** number of readings N reduced from 1,000,000 to 1,000.

| N | Loop time | Vectorized time | Speed-up |
|---|---|---|---|
| 1,000,000 | 0.171 s | 0.0039 s | about 44× |
| 1,000 | 0.000197 s | 0.0000060 s | about 33× |

**Explanation:** the absolute times fall in proportion to N, but vectorization stays far faster at both sizes. A loop pays Python interpreter overhead for every element, while NumPy runs one compiled C loop over the whole array.

## D. Meaning of the output

- The first squared values (0.0379, 0.0127, 0.0464, 0.0309, 0.0008 s²) are the readings in seconds squared, so a 194.6 ms reading gives 0.0379.
- Both versions return identical numbers, so vectorization is faster but not less accurate.
- Identity check: max |sin²x + cos²x − 1| over one million points is 2.2 × 10⁻¹⁶. That is machine precision, so the identity holds to the limit of floating-point storage.

## E. Related real-world case: ADC samples to RMS voltage

**Assumptions:** a 12-bit ADC outputs integer counts 0 to 4095 that map linearly to 0 to 3.3 V. Counts are random (uniform) to simulate a noisy signal. RMS = √(mean(V²)).

**Input data:** 2,000,000 simulated samples.

**Output:**

| Quantity | Loop | Vectorized |
|---|---|---|
| RMS voltage | 1.905799 V | 1.905799 V |
| Time | 2.45 s | 0.0152 s |
| Speed-up | | about 161× |

**Interpretation:** the RMS of a uniform 0 to 3.3 V signal is about 3.3/√3 = 1.905 V, which matches. The savings grow with larger data sets, which is why signal processing code is vectorized.
