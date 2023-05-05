import math
import numpy as np
import matplotlib.pyplot as plt

plt.xlabel('k')
plt.ylabel('F(Z=k)')
Rand_Variables = [0,1,2,3,4,5,6]
Cumm_Prob = [0.046656,0.23328,0.54432,0.8208,0.95904,0.995904,1]
plt.xlim([-1,7])
plt.ylim([-0.5,1.5])
plt.scatter(Rand_Variables,Cumm_Prob,marker='o')


plt.show()
