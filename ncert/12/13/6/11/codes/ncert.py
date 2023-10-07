from scipy.stats import bernoulli
import numpy as np

# Simulating random outcomes
x1 = bernoulli.rvs(size=1000000, p=1/6)
x2 = bernoulli.rvs(size=1000000, p=1/6)
x3 = bernoulli.rvs(size=1000000, p=1/6)

# Counting occurrences of each outcome
c1 = np.sum(x1 == 1)
c2 = np.sum((x1 == 0) & (x2==1))
c3 = np.sum((x1 == 0) & (x2 == 0) & (x3 == 1))
c4 = np.sum((x1 == 0) & (x2 == 0) & (x3 == 0))

# Calculating probabilities
p1 = c1 / 1000000
p2 = c2 / 1000000
p3 = c3 / 1000000
p4 = c4 / 1000000

# Calculating expected money using probabilies
money = (p1 * 1) + (p2 * 0) + (p3 * (-1)) + (p4 * (-3))
print(money)
