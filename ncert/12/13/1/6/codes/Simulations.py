import numpy as np
from scipy.stats import bernoulli

n_trials = 100000

X = bernoulli.rvs(p=0.5, size=(n_trials, 1, 3))

# 1- heads, 0 - Tails
# (A) E: head on third toss, F: heads on first two tosses
F_a = (X[:, 0, 0] == 1) & (X[:, 0, 1] == 1)
EF_a = np.sum((X[:, 0, 2] == 1) & F_a)
Pr_E_given_F_a = EF_a / np.sum(F_a)
print("Pr(E|F) for (a) is:", Pr_E_given_F_a)

# (B) E: at least two heads, F: at most two heads
F_b = np.sum(X == 1, axis=2) <= 2
EF_b = np.sum((np.sum(X, axis=2) >= 2) & F_b)
Pr_E_given_F_b = EF_b / np.sum(F_b)
print("Pr(E|F) for (b) is:", Pr_E_given_F_b)

# (C) E: at most two tails, F: at least one tail
F_c = np.sum(X == 0, axis=2) >= 1
EF_c = np.sum((np.sum(X == 0, axis=2) <= 2) & F_c)
Pr_E_given_F_c = EF_c / np.sum(F_c)
print("Pr(E|F) for (c) is:", Pr_E_given_F_c)