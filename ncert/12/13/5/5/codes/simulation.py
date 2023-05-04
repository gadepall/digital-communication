
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
simlen=10000000
#number of bulbs
n =  5

#Probability of bulb to fuse  
p = 0.05

experiment=np.zeros(4)
acctual=np.zeros(4)
data_binom = binom.rvs(n,p,size=simlen)  #Simulating the event of jumping 10 hurdles
defects,stimulation = np.unique(data_binom , return_counts= True)

stimulation = np.cumsum(stimulation)/simlen

experiment[0]=stimulation[0] 
experiment[1]=stimulation[1]
experiment[2]=stimulation[5]-stimulation[1]
experiment[3]=stimulation[5]-stimulation[0]
acctual[0]=binom.cdf(0,n,p) 
acctual[1]=binom.cdf(1,n,p)
acctual[2]=binom.cdf(5,n,p)-binom.cdf(1,n,p)
acctual[3]=binom.cdf(5,n,p)-binom.cdf(0,n,p)

print("For answer 1 stimulation value is "+str(experiment[0])+" and acctual value is "+str(acctual[0]))
print("For answer 2 stimulation value is "+str(experiment[1])+" and acctual value is "+str(acctual[1]))
print("For answer 3 stimulation value is "+str(experiment[2])+" and acctual value is "+str(acctual[2]))
print("For answer 4 stimulation value is "+str(experiment[3])+" and acctual value is "+str(acctual[3]))
