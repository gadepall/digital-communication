import numpy as np
import math
from scipy.stats import bernoulli

simlen = 1000000

pA = 0.5
pB = 0.3
data_bern = bernoulli.rvs(size=simlen,p=pA+pB)
err_ind = np.nonzero(data_bern == 1)
prob = 1-np.size(err_ind)/simlen
print("Probability - simulation, actual :", prob,1-pA-pB)
