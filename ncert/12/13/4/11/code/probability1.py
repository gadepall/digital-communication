import numpy as np
import random
#therotical
k = [0,1,2]                   # random variable
P_k = [25/36,10/36,1/36] # PDF             

mean_calculated = k[0]*P_k[0]+k[1]*P_k[1]+k[2]*P_k[2]
print("Mean of getting six on dice", mean_calculated)


# Sample size
simlen = 1000

# Possible outcomes
n = [6]

# Generate X1 and X2
y = np.random.randint(1, 7, size=(2, simlen))
#print(y)
# Count the number of sixes rolled in each sample
num_sixes = np.sum(y == 6, axis=0)
#print(num_sixes)
# Calculate the mean number of sixes
mean_sixes = np.mean(num_sixes)

print("simulated mean=",mean_sixes)
