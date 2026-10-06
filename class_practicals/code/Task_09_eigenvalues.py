"""Task 9 - Eigenvalues and Eigenvectors
PART 1 original | PART 2 changed network | PART 3 related case (PageRank by power iteration)"""
import numpy as np

nodes = ["A", "B", "C", "D"]
def centrality(A):
    w, V = np.linalg.eig(A)
    i = np.argmax(np.real(w))
    lam = np.real(w[i]); v = np.real(V[:, i])
    c = np.abs(v) / np.abs(v).sum()
    return lam, v, c

print("=== PART 1: Original ===")
A = np.array([[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0]], dtype=float)
lam, v, c = centrality(A)
print("Dominant eigenvalue:", lam)
print("Eigenvector-based importance:")
for n_, s in zip(nodes, c):
    print(f"{n_}: {s:.4f}")
print("Verification error:", np.linalg.norm(A @ v - lam * v))
print("All eigenvalues:", np.round(np.sort(np.real(np.linalg.eigvals(A)))[::-1], 4))

print("\n=== PART 2: Changed input - add link A-D ===")
A2 = A.copy(); A2[0, 3] = A2[3, 0] = 1
lam2, v2, c2 = centrality(A2)
print("Dominant eigenvalue:", round(lam2, 4), "(was", round(lam, 4), ")")
for n_, s in zip(nodes, c2):
    print(f"{n_}: {s:.4f}")

print("\n=== PART 3: Related case - PageRank for 5 web pages (damping 0.85) ===")
pages = ["Home", "News", "Blog", "Shop", "About"]
# links[i, j] = 1 if page j links to page i
links = np.array([
    [0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
], dtype=float)
M = links / links.sum(axis=0)              # column-stochastic
d, n = 0.85, 5
G = d * M + (1 - d) / n * np.ones((n, n))  # Google matrix
r = np.ones(n) / n
for it in range(1, 200):
    r_new = G @ r
    if np.linalg.norm(r_new - r, 1) < 1e-12:
        break
    r = r_new
print(f"Power iteration converged in {it} steps")
w, V = np.linalg.eig(G)
ev = np.real(V[:, np.argmax(np.real(w))]); ev = ev / ev.sum()
for p, s, s2 in sorted(zip(pages, r, ev), key=lambda t: -t[1]):
    print(f"{p:6s} PageRank = {s:.4f} (eigenvector method {s2:.4f})")
print("Dominant eigenvalue of Google matrix:", round(np.max(np.real(w)), 6))
