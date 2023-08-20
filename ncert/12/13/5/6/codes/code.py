import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

#100 samples
simlen=int(1e2)

#One event is taking 4 balls from bag with replacement
#Probability of the event that non of the balls are zero i.e pX(0)=(0.9)^4 which is denoted by 1 in the simulation
prob = (0.9)**4

#Generating sample date using Bernoulli r.v.
data_bern = bernoulli.rvs(size=simlen,p=prob)
#Calculating the number of favourable outcomes
err_ind = np.nonzero(data_bern == 1)
#calculating the probability
err_n = np.size(err_ind)/simlen

#Simulation Vs Theory  
print("Simulated = ",err_n,"Theorical = ",prob)
print(data_bern)

