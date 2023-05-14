import math
import numpy as np
import matplotlib.pyplot as plt

# Probability distribution function 
#X axis is values of random variables 
#Y axis will contain probability of that points according to random variables
# distance between P and Q is d.
plt.xlabel('k')
plt.ylabel('P(Z=k)')
Rand_Variables = [0,1,2,3,4,5,6]
Prob = [0.046656,0.186624,0.31104,0.27648,0.13824,0.036864,0.004096]
plt.xlim([-1,7])
plt.ylim([0,1])
plt.scatter(Rand_Variables,Prob,marker='o')


plt.show()
