import math
import numpy as np
from scipy.stats import bernoulli

simlen = 100000

print("Value equal to 7:")
p1 = 0.1
data_bern1 = bernoulli.rvs(size=simlen,p=p1)
err_ind1 = np.nonzero(data_bern1 == 1)
print("Probability-simulation,actual:",np.size(err_ind1)/100000,p1)
print("Simulated values: ", data_bern1)

print("Value greater than 7:")
p2 = 0.3
data_bern2 = bernoulli.rvs(size=simlen ,p=p2)
err_ind2 = np.nonzero(data_bern2 == 1)
print("Probability-simulation,actual:",np.size(err_ind2)/100000,p2)
print("Simulated values: ", data_bern2)

print("Value less  than 7:")
p3 = 0.6
data_bern3 = bernoulli.rvs(size=simlen ,p=p3)
err_ind3 = np.nonzero(data_bern3 == 1)
print("Probability-simulation,actual:",np.size(err_ind3)/100000,p3)
print("Simulated values: ", data_bern3)
