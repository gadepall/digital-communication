import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
simlen=10000000
#Number of die rolls
n = 6

#Probability of odd number  
p = 1/6

experiment=0
actual=0
data_binom = binom.rvs(n,p,size=simlen)
defects,stimulation = np.unique(data_binom , return_counts= True)

stimulation = np.cumsum(stimulation)/simlen

experiment=stimulation[2] 
actual=binom.cdf(2,n,p) 

print("For answer 1 stimulation value is "+str(experiment)+" and actual value is "+str(actual))
