import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
simlen=10000000
#number of trials
n =  6

#Probability of Ball with mark 'X' getting chosen round(
p = 0.4

experiment=np.zeros(4)
acctual=np.zeros(4)
data_binom = binom.rvs(n,p,size=simlen)  #Simulating the event of jumping 10 hurdles
defects,stimulation = np.unique(data_binom , return_counts= True)

stimulation = np.cumsum(stimulation)/simlen

experiment[0]=stimulation[6]-stimulation[5] 
experiment[1]=1-stimulation[3]
experiment[2]=stimulation[5]
experiment[3]=stimulation[4]-stimulation[3]
acctual[0]=binom.cdf(6,n,p)-binom.cdf(5,n,p) 
acctual[1]=1-binom.cdf(3,n,p)
acctual[2]=binom.cdf(5,n,p)
acctual[3]=binom.cdf(4,n,p)-binom.cdf(3,n,p)

print("For answer 1 stimulation value is "+str(round(experiment[0],4))+" and acctual value is "+str(round(acctual[0],4)))
print("For answer 2 stimulation value is "+str(round(experiment[1],4))+" and acctual value is "+str(round(acctual[1],4)))
print("For answer 3 stimulation value is "+str(round(experiment[2],4))+" and acctual value is "+str(round(acctual[2],4)))
print("For answer 4 stimulation value is "+str(round(experiment[3],4))+" and acctual value is "+str(round(acctual[3],4)))