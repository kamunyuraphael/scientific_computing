# Task 11 – Root Finding: Newton-Raphson and Secant Methods

**Program:** `code/Task_11_newton_secant.py` · **Output:** `outputs/Task_11_newton_secant.txt`

---

## B. Input values and mathematical operation

| Item | Detail |
|---|---|
| Cash flows | −10000 (year 0), then 3000, 3500, 4000, 2500 |
| Function | NPV(r) = Σ CFₜ / (1+r)ᵗ; the IRR is the rate with NPV(r) = 0 |
| Newton-Raphson | rₙ₊₁ = rₙ − NPV(rₙ)/NPV′(rₙ), start 0.10 |
| Secant | Same idea with the derivative replaced by the slope through two points (starts 0.05 and 0.20) |

**Results:** IRR = **11.542461 %** from both methods; NPV at the solution is 0.000000. Newton took 4 iterations and secant 7. Manual Newton iterates: 0.10000000 → 0.11502117 → 0.11542433 → 0.11542461.

Textbook check: f(x) = x² − 2 from x₀ = 1.5 gives 1.416667, 1.414216, 1.414214 (√2).

## C. Parameter change

| Change | Result |
|---|---|
| Final inflow 2500 → 5500 | IRR rises from 11.54 % to 19.51 % |
| Newton start 0.10 | root found in 4 iterations |
| Newton start 0.50 | root found in 8 iterations |
| Newton start 2.0 | diverges (no valid root) |

**Explanation:** larger inflows make the project more profitable, so the break-even discount rate rises. Newton converges quickly from a reasonable start but a poor start can send it to nonsense, which a bracketing method (Task 10) never does.

## D. Meaning of the output

- IRR 11.54 % means the project earns that annual return. If the required return is less than 11.54 %, the project is worth doing.
- The number of correct digits roughly doubles each Newton step (0.1150 → 0.115424 → 0.1154246), which is quadratic convergence.

## E. Related real-world case: finding the interest rate of a loan

**Assumptions:** a loan of 12,000 is repaid with 36 monthly payments of 380. The monthly rate r satisfies 12000 = 380 · (1 − (1+r)⁻³⁶)/r.

**Output:**

| Quantity | Value |
|---|---|
| Monthly rate (Newton, 6 iterations) | 0.726144 % |
| Monthly rate (secant, 7 iterations) | 0.726144 % |
| Nominal APR (12 × monthly) | 8.7137 % |
| Effective annual rate | 9.0703 % |
| Total repaid / interest paid | 13,680 / 1,680 |
| Check: payment at the root | 380.000000 |

**Interpretation:** the rate cannot be isolated by algebra, so a numerical method is needed. The effective rate is higher than the nominal APR because of monthly compounding.
