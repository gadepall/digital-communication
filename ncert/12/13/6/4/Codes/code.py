import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
simlen=10000000
#number of people in random sample.
n =  10

#Probability that the choosen person is right-handed.
p = 0.9

experiment=np.zeros(1)
acctual=np.zeros(1)
data_binom = binom.rvs(n,p,size=simlen) 
defects,stimulation = np.unique(data_binom , return_counts= True)
if (len(stimulation) == 8):
	stimulation = np.insert(stimulation,0,0)
	stimulation = np.insert(stimulation,0,0)
	stimulation = np.insert(stimulation,0,0)
if (len(stimulation) == 9):
	stimulation = np.insert(stimulation,0,0)
	stimulation = np.insert(stimulation,0,0)
if (len(stimulation) == 10):
	stimulation = np.insert(stimulation,0,0)
stimulation = np.cumsum(stimulation)/simlen
experiment[0]=stimulation[6]
acctual[0]=binom.cdf(6,n,p)

print("For answer  stimulation value is "+str(round(experiment[0],4))+" and acctual value is "+str(round(acctual[0],4)))
