
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

#Number of samples is 24, 1 denotes red ball and 0 denotes non-red ball
simlen=int(24)

#Probability of the event ball is red, i.e., X=0 is 1/6
prob = 1/6

#Generating sample date using Bernoulli r.v.
data_bern = bernoulli.rvs(size=simlen,p=prob)
#Calculating the number of favourable outcomes(non-red)
err_ind = np.nonzero(data_bern == 0)
#calculating the probability
err_n = np.size(err_ind)/simlen
print("simulation : ",data_bern)
print("Probability from simulation : ",err_n)
print("Theoretical probability : ",(1-prob))
print("")




#number of sample is 24 , 1 denotes white ball and 0 denotes non-white ball
simlen=int(24)
#probability ofthe event ball is white ,i.e X=1 is 1/3
prob =1/3
#generating sample simulation
data_bern = bernoulli.rvs(size=simlen,p=prob)
#calculating number of favourable outcome(white ball)
err_ind = np.nonzero(data_bern == 1)
#calculating the probability
err_n = np.size(err_ind)/simlen
print("simulation : ",data_bern)
print("Probability from simulation : ",err_n)
print("Theoretical probability : ",prob)
