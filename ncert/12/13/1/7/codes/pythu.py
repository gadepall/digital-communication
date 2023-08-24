import numpy as np
from scipy.stats import bernoulli

# Simulate random variables
x1 = bernoulli.rvs(size=10000, p=0.5)
x2 = bernoulli.rvs(size=10000, p=0.5)

# F1:head appears on one coin so, other is tail
# x1==1 and x2==0 or x1==0 and x2==1, so, its x1.x2'+x1'x2 which is xor gate
countF1 = np.sum(np.logical_xor(x1, x2))

# F2: no head appears
# x1==0 and x2==0 
countF2 = np.sum(np.logical_and(x1==0 , x2 == 0))

#I1: intersection of E and F where i.e, xor of x1 and x2 and xor of x1' and x2'
countI1 = np.sum(np.logical_and(np.logical_xor(x1, x2), np.logical_xor(1 - x1, 1 - x2)))

#I2: intersection of E and F where i.e, logical and of (both coins show head) and (both coins show tail)
countI2 = np.sum(np.logical_and(np.logical_and(x1 == 0, x2 == 0), np.logical_and(x1 == 1, x2 == 1)))

# Calculate conditional probabilities
prob_I1_given_F1 = countI1 / countF1
prob_I2_given_F2 = countI2 / countF2

print("1) P(E|F) = " +str(prob_I1_given_F1))
print("2) P(E|F) = " +str(prob_I2_given_F2))
