# Task 19 – Numerical Optimization

**Program:** `code/Task_19_optimization.py` · **Output:** `outputs/Task_19_optimization.txt`

---

## B. Input values and mathematical operation

| Item | Detail |
|---|---|
| Objective | Minimize cost = 12x + 18y (x = Type A units, y = Type B units) |
| Constraint | Capacity 100x + 170y ≥ 1000 |
| Bounds | x ≥ 0 and y ≥ 0 |
| Solver | `minimize(method="SLSQP")` from the start point (5, 3) |
| Integer check | Search whole-number combinations 0 to 19 |

Warm-up: f(x) = (x − 3)² + 2 gives the minimum at x = 3 with value 2.

**Results:** Type A = 0, Type B = 5.882, capacity exactly 1000, minimum cost **105.88**. Best whole-server plan: 0 of A and 6 of B (cost 108, capacity 1020).

## C. Parameter change

| Change | Result |
|---|---|
| Type B cost 18 → 24 | A = 10, B = 0, cost 120 (A is now cheaper per capacity unit) |
| Requirement 1000 → 1500 | B = 8.824, cost 158.82; whole servers: 9 of B, cost 162 |

**Explanation:** cost per unit of capacity is 12/100 = 0.120 for A and 18/170 = 0.106 for B, so B wins originally. At cost 24, B costs 0.141 per unit and the answer flips to A. A linear objective always chooses the cheapest per-unit option, and the capacity constraint is exactly met (active).

## D. Meaning of the output

- The optimum sits on the constraint boundary (capacity exactly 1000), because extra capacity only adds cost.
- The whole-server answer (108) is slightly above the continuous optimum (105.88). That gap is the price of integer rounding.

## E. Related real-world case: maximizing factory profit

**Assumptions:** a factory makes tables (x) and chairs (y). Profit is 40 per table and 30 per chair. Machine time: 2x + y ≤ 100 hours. Labour: x + y ≤ 80 hours. At most 40 tables. Since SciPy minimizes, the negative of profit is minimized.

**Output:**

| Quantity | Value |
|---|---|
| Tables / chairs | 20 / 60 |
| Maximum profit | 2600 |
| Machine hours used | 100 of 100 (binding) |
| Labour used | 80 of 80 (binding) |
| Table limit | 20 of 40 (slack) |
| With 120 machine hours | 40 tables, 40 chairs, profit 2800 |

**Interpretation:** the optimum is at the corner where the machine and labour constraints meet. The table limit is not a bottleneck. Adding 20 machine hours raises profit by 200, so each extra machine hour is worth about 10 (a "shadow price", valid in this range). The integer check gives the same answer.
