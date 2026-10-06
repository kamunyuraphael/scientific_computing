# Task 4 – Floating-Point Arithmetic and Numerical Errors

**Program:** `code/Task_04_numerical_errors.py` · **Output:** `outputs/Task_04_numerical_errors.txt`

---

## B. Input values and mathematical operation

| Item | Detail |
|---|---|
| Inputs | 0.1, 0.2, 0.3; true value √2 and approximation 1.414; x = 10⁻⁴, 10⁻⁸, 10⁻¹² |
| Operations | Exact equality test vs `np.isclose`; absolute error \|true − approx\|; relative error = absolute / \|true\|; two algebraically equal formulas for (√(1+x) − 1)/x |

## C. Parameter change

**Change 1:** approximation of √2 improved.

| Approximation | Absolute error | Relative error |
|---|---|---|
| 1.414 | 2.14 × 10⁻⁴ | 0.0151 % |
| 1.4142 | 1.36 × 10⁻⁵ | 0.0010 % |
| 1.41421 | 3.56 × 10⁻⁶ | 0.0003 % |

**Change 2:** x made even smaller (10⁻¹⁴, 10⁻¹⁶). The direct formula gives 0.4885 at 10⁻¹⁴ and exactly 0 at 10⁻¹⁶. The stable formula still gives 0.5.

**Explanation:** more correct digits reduce truncation error. But when x is tiny, √(1+x) is stored as exactly 1 (or almost), so subtracting 1 destroys the significant digits. This is called catastrophic cancellation, a round-off error.

## D. Meaning of the output

- `0.1 + 0.2 = 0.30000000000000004`, so `== 0.3` is `False`. Binary cannot store 0.1 or 0.2 exactly. `np.isclose` returns `True` because it accepts a tiny tolerance.
- Absolute error 0.00021356 and relative error 0.0151 % match the worked example in the brief.
- At x = 10⁻¹² the direct formula gives 0.500044 while the stable formula gives 0.500000 (the true limit is 0.5). The two formulas are equal in algebra but not in a computer.

## E. Related real-world case: banking balance accumulation

**Assumptions:** a system adds a 0.10 fee one million times. Exact total is 100,000.

| Method | Result |
|---|---|
| Naive `+=` loop | 100000.0000013329 (error 1.33 × 10⁻⁶) |
| `math.fsum` | 100000.0000000000 |
| `Decimal` | 100000.00 |
| `naive == 100000` | False (but `np.isclose` is True) |

**Interpretation:** tiny per-step errors accumulate. For money, use `Decimal` or integer cents. For scientific sums, use `math.fsum`. Never test floats with `==`.
