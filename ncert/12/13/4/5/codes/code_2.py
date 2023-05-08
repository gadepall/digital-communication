import numpy as np
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
simlen=10000000
#number of trials
n =  2

#Probability of getting 6 in a die toss
p = 0.166666666667

experiment=np.zeros(3)
actual=np.zeros(3)
data_binom = binom.rvs(n,p,size=simlen)  #Simulating the event
defects,stimulation = np.unique(data_binom , return_counts= True)

stimulation = np.cumsum(stimulation)/simlen

experiment[0]=stimulation[2]-stimulation[0] 
experiment[1]=stimulation[0]

actual[0]=binom.cdf(2,n,p)-binom.cdf(0,n,p) 
actual[1]=binom.cdf(0,n,p)
print("simulation value of probability of success is "+str(round(experiment[0],4))+" and actual value is "+str(round(actual[0],4)))
print("simulation value of probability of no success is "+str(round(experiment[1],4))+" and actual value is "+str(round(actual[1],4)))
