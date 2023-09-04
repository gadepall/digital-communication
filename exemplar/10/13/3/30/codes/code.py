import math
import numpy as np
from scipy.stats import bernoulli

simlen = 1000000

pmf = np.full(10,0.1)

def cdf(k):
    if(k>10):
        return 1
    elif(k<=0):
        return 0
    else:
        return k*0.1

print("Value equal to 7:")
p1 = pmf[7]
data_bern1 = bernoulli.rvs(size=simlen,p=p1)
err_ind1 = np.nonzero(data_bern1 == 1)
print("Probability-simulation,actual:",round(np.size(err_ind1)/simlen,4),round(p1,2))
#print("Simulated values: ", data_bern1)

print("Value greater than 7:")
p2 = cdf(10)-cdf(7)
data_bern2 = bernoulli.rvs(size=simlen ,p=p2)
err_ind2 = np.nonzero(data_bern2 == 1)
print("Probability-simulation,actual:",round(np.size(err_ind2)/simlen,4),round(p2,2))
#print("Simulated values: ", data_bern2)

print("Value less  than 7:")
p3 = cdf(6)
data_bern3 = bernoulli.rvs(size=simlen ,p=p3)
err_ind3 = np.nonzero(data_bern3 == 1)
print("Probability-simulation,actual:",round(np.size(err_ind3)/simlen, 4),round(p3,2))
#print("Simulated values: ", data_bern3)
