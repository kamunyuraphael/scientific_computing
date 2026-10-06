# Task 20 – Random Numbers and Monte Carlo Methods

**Program:** `code/Task_20_monte_carlo.py` · **Figure:** `figures/task20_monte_carlo.png`

---

## B. Input values and mathematical operation

| Item | Detail |
|---|---|
| Input | Demand ~ Normal(mean 850, standard deviation 120); capacity 1000; N = 100,000 simulations; seed 42 |
| Operation | Generate random demands, mark those above capacity, and estimate P(overload) = overloaded / N |
| Validation | Exact answer 1 − Φ((1000 − 850)/120) from the normal distribution |

**Results:** 10,616 overloads out of 100,000, so the estimate is **10.616 %**. Exact value 10.565 %. Standard error = √(p(1−p)/N) = 0.097 %, giving a 95 % interval of [10.43 %, 10.81 %], which contains the exact answer.

Warm-up π estimates (points in a quarter circle): N = 1,000 gives 3.084; N = 100,000 gives 3.150; N = 5,000,000 gives 3.142.

## C. Parameter change

| Capacity | N = 1,000 | N = 100,000 | Exact |
|---|---|---|---|
| 900 | 31.70 % | 33.47 % | 33.85 % |
| 1000 | 8.70 % | 10.33 % | 10.57 % |
| 1150 | 0.60 % | 0.61 % | 0.62 % |

Also, increasing the spread of demand from 120 to 200 raises the overload probability to 22.4 % (exact 22.7 %).

**Explanation:** more simulations give estimates closer to the exact value (error shrinks like 1/√N). Greater variability in demand means more chances of exceeding capacity. For rare events (such as 0.6 %) many simulations are needed, because only a few runs produce the event.

## D. Meaning of the output and graph

- About one request peak in nine would overload the server at capacity 1000.
- **Graph (left):** the running estimate jumps around widely for small N, then settles toward the red dashed line (exact value). This is the law of large numbers.

## E. Related real-world case: project deadline risk

**Assumptions:** a project has three tasks done in sequence, each with an uncertain duration (triangular distribution of minimum, most likely, maximum days): design (5, 8, 14), build (10, 14, 24), testing (4, 6, 12). Deadline: 30 days. 200,000 simulations (seed 2026).

**Output:**

| Quantity | Value |
|---|---|
| Mean total duration | 32.31 days (standard deviation 3.88) |
| Median / 90th / 95th percentile | 32.13 / 37.50 / 39.02 days |
| P(finish later than 30 days) | **70.6 %** |

| Deadline | 26 | 28 | 30 | 32 | 35 |
|---|---|---|---|---|---|
| P(late) | 95.8 % | 86.5 % | 70.6 % | 51.3 % | 24.5 % |

**Interpretation:** adding the "most likely" durations gives 28 days, which looks safe against a 30-day deadline. But each task has a long upper tail, so the average is 32.3 days and the project is late about 7 times in 10. To be 90 % sure, promise about 37.5 days. The right-hand histogram shows most of the probability mass lying to the right of the red deadline line.
