# Task 9 – Eigenvalues and Eigenvectors

**Program:** `code/Task_09_eigenvalues.py` · **Output:** `outputs/Task_09_eigenvalues.txt`

---

## B. Input values and mathematical operation

| Item | Detail |
|---|---|
| Input | Adjacency matrix of a 4-node network. Links: A–B, A–C, B–C, B–D, C–D |
| Operation | Solve Av = λv with `np.linalg.eig`; take the largest eigenvalue and its eigenvector; normalize so the scores add to 1 |

**Results:**

| Quantity | Value |
|---|---|
| Dominant eigenvalue λ | 2.5616 (= (1 + √17)/2) |
| Importance A, B, C, D | 0.2192, 0.2808, 0.2808, 0.2192 |
| Verification ‖Av − λv‖ | 1.9 × 10⁻¹⁵ |
| All eigenvalues | 2.5616, 0, −1, −1.5616 |

## C. Parameter change

**Change:** add the missing link A–D (the network becomes fully connected).

| Quantity | Original | Changed |
|---|---|---|
| Dominant λ | 2.5616 | 3.0 |
| Scores A, B, C, D | 0.219, 0.281, 0.281, 0.219 | 0.25 each |

**Explanation:** with every node linked to every other, no node is more central, so scores become equal. λ = 3 = n − 1 for a complete graph of 4 nodes.

## D. Meaning of the output

- B and C are the most influential nodes because each connects to three others; A and D connect to only two.
- The verification error near 10⁻¹⁵ shows A·v really equals λ·v: A only stretches v by 2.56 without turning it.

## E. Related real-world case: PageRank for five web pages

**Assumptions:** links: Home → News, Blog; News → Home, Blog; Blog → Home, Shop; Shop → Home, About; About → Home. Damping factor d = 0.85 (a surfer follows a link 85 % of the time and jumps to a random page 15 %). Google matrix G = d·M + (1−d)/n, where M is the link matrix with each column divided by its page's outgoing links.

**Output (power iteration converged in 35 steps and matched the eigenvector method):**

| Page | PageRank |
|---|---|
| Home | 0.3456 |
| Blog | 0.2521 |
| News | 0.1769 |
| Shop | 0.1371 |
| About | 0.0883 |

The dominant eigenvalue of G is exactly 1.

**Interpretation:** Home ranks highest because all four other pages link to it. The scores sum to 1, so each is the long-run share of visits. The eigenvalue 1 shows the ranking is a stable steady state.
