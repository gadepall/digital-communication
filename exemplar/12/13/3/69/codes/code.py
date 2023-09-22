import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

#100 samples
simlen=int(1e2)

probB = (4/9)
probA = (3/5)

#Generating sample date using Bernoulli r.v.
data_bernA = bernoulli.rvs(size=simlen,p=probA)
#Calculating the number of favourable outcomes
err_indA = np.nonzero(data_bernA == 1)
#calculating the probability
err_nA = np.size(err_indA)/simlen

#Generating sample date using Bernoulli r.v.
data_bernB = bernoulli.rvs(size=simlen,p=probB)
#Calculating the number of favourable outcomes
err_indB = np.nonzero(data_bernB == 1)
#calculating the probability
err_nB = np.size(err_indB)/simlen

#C=A'B'
data_bernC = data_bernA+data_bernB 
err_indC = np.nonzero(data_bernB+data_bernA == 0) #C=(A+B)'  
err_nC = np.size(err_indC)/simlen 
probC= 1 - probA - probB + probA*probB

#Simulation Vs Theory  
print("Simulated = ",err_nC,"Theorical = ",probC)
print("In this array 0 represents favourable outcome")
print(data_bernC) # no of zeros represents the favourable outcomes

