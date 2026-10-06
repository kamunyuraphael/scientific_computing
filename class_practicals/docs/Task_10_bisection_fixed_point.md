# Task 10 – Root Finding: Bisection and Fixed-Point Methods

**Program:** `code/Task_10_bisection_fixed_point.py` · **Figure:** `figures/task10_roots.png`

---

## B. Input values and mathematical operation

| Item | Detail |
|---|---|
| Function | f(T) = T − 25 − 10·e^(−T/20); root means heat gain equals heat loss |
| Bisection | Bracket [20, 40] (f(20) < 0, f(40) > 0); repeatedly halve the interval, keep the half where the sign changes; tolerance 10⁻¹⁰ |
| Fixed point | Rewrite as T = g(T) = 25 + 10·e^(−T/20); iterate Tₙ₊₁ = g(Tₙ) from T₀ = 30 |

**Results:** both methods give **27.525211 °C**. Fixed point needed 13 iterations; bisection needed 37 halvings (20 / 2³⁷ ≈ 1.5 × 10⁻¹⁰). Fixed point converges because |g′(T*)| = 0.126 < 1.

## C. Parameter change

**Change:** ambient 25 → 35 and heat source 10 → 40, i.e. f(T) = T − 35 − 40·e^(−T/20), bracket [20, 80].

| Quantity | Original | Changed |
|---|---|---|
| Equilibrium | 27.525 °C | 40.326 °C |
| Fixed-point iterations | 13 | 21 |
| \|g′\| at the root | 0.126 | 0.266 |

Bisection effort versus tolerance: 17 halvings for 10⁻⁴, 44 halvings for 10⁻¹².

**Explanation:** the new equilibrium is hotter. The slope |g′| is larger, so fixed-point iteration converges more slowly. Bisection cost depends only on the interval size and tolerance (about log₂(width/tolerance)), not on the function.

## D. Meaning of the output and graph

- **Graph (left):** the curve crosses zero at 27.53 °C (the dashed line). Below that, heat loss dominates (negative); above it, heat gain dominates.
- Bisection is slow but guaranteed; fixed point is fast only when |g′| < 1.

## E. Related real-world case: break-even points

**Assumptions:** profit for q units is profit(q) = 300·√q − 4000 − 5q (revenue grows with diminishing returns; 4000 fixed cost; 5 per unit variable cost). A break-even is a root of profit(q).

**Output:**

| Quantity | Value |
|---|---|
| Lower break-even (bracket [100, 1000]) | 400 units |
| Upper break-even (bracket [1000, 2500]) | 1600 units |
| Profit at 1000 units | 486.83 |
| Maximum profit (at 900 units) | 500 |

**Interpretation:** the business only makes a profit between 400 and 1600 units. Because there are two roots, each needs its own sign-changing bracket. Beyond 1600 units, variable cost outgrows revenue. The right-hand graph is an upside-down U that crosses zero twice.
