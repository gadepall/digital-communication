import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
simlen=10000000
#Number of die rolls
n = 6

#Probability of odd number  
p = 0.5

experiment=np.zeros(4)
actual=np.zeros(4)
data_binom = binom.rvs(n,p,size=simlen)
defects,stimulation = np.unique(data_binom , return_counts= True)

stimulation = np.cumsum(stimulation)/simlen

experiment[0]=stimulation[5]-stimulation[4] 
experiment[1]=stimulation[6]-stimulation[4]
experiment[2]=stimulation[5]
actual[0]=binom.cdf(5,n,p)-binom.cdf(4,n,p) 
actual[1]=binom.cdf(6,n,p)-binom.cdf(4,n,p)
actual[2]=binom.cdf(5,n,p)

print("For answer 1 stimulation value is "+str(experiment[0])+" and actual value is "+str(actual[0]))
print("For answer 2 stimulation value is "+str(experiment[1])+" and actual value is "+str(actual[1]))
print("For answer 3 stimulation value is "+str(experiment[2])+" and actual value is "+str(actual[2]))
