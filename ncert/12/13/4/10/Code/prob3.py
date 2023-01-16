import numpy as np
import random

k = [0,1,2,3]                   # random variable
P_k = [0.125,0.375,0.375,0.125] # PDF             
trials = 1000

mean_calculated = k[0]*P_k[0]+k[1]*P_k[1]+k[2]*P_k[2]+k[3]*P_k[3]
print("Mean number of heads in three tosses of a coin is", mean_calculated)


#Simulating samples 
#S = np.random.randint(k[0],k[3] + 1, size=trials) 
S = np.random.choice(k, p=P_k, size=trials)          
Samples = list(S)

#Generating PDF through simulated samples
P_0 = Samples.count(0)/trials
P_1 = Samples.count(1)/trials
P_2 = Samples.count(2)/trials
P_3 = Samples.count(3)/trials


mean_simulated = k[0]*P_0+k[1]*P_1+k[2]*P_2+k[3]*P_3
print("Mean through simulation is", mean_simulated)
  
    


