import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
simlen=10000000
#number of trials
n =  3

#probability og getting odd number on dice
p = 0.5

experiment=np.zeros(1)
acctual=np.zeros(1)
data_binom = binom.rvs(n,p,size=simlen)  #Simulating the event 
defects,stimulation = np.unique(data_binom , return_counts= True)

stimulation = np.cumsum(stimulation)/simlen

experiment[0]=stimulation[3]-stimulation[0] 
acctual[0]=binom.cdf(3,n,p)-binom.cdf(0,n,p) 

print("For answer  stimulation value is "+str(round(experiment[0],4))+" and acctual value is "+str(round(acctual[0],4)))
