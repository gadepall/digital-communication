import numpy as np                                
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

#Number of tickits is 40, 1 number divisible by 5 and 0 denotes number not divisible by 5
simlen=int(1000)

#Probability of the randomly selected ticket number as multiple of 5  i.e., X=1 is 1/8
prob = 1/8

#Generating sample date using Bernoulli r.v.
data_bern = bernoulli.rvs(size=simlen,p=prob)
#Calculating the number of favourable outcomes
err_ind = np.nonzero(data_bern == 1)
#calculating the probability
err_n = round(np.size(err_ind)/simlen,4)
print(f'simulated probaility is {err_n}')        
if err_n == prob:
    print(f'simulated and theopritcal probabilities same and equal to {prob}')
