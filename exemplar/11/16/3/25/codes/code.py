import numpy as np
import math
from scipy.stats import bernoulli

simlen = 1000000

n = 12
N = math.factorial(n)

def pmf(k):
    return math.factorial(13-k)*math.factorial(k)/N

prob = pmf(6)
data_bern = bernoulli.rvs(size=simlen,p=prob)
err_ind = np.nonzero(data_bern == 1)

print("Probability - simulation, actual :", np.size(err_ind)/simlen,prob)
