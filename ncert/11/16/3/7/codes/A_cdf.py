import math
import numpy as np
import matplotlib.pyplot as plt


plt.xlabel('k')
plt.ylabel('Pr(A<=k)')
Amount = [-6,-3,-1,1.5,4,5]
Prob = [0.0625,0.25,0.375,0.25,0.0625,0]
cdf_A=np.cumsum(Prob)
plt.stem(Amount,cdf_A)
plt.xlim([-8,6])
plt.ylim([0,1.1])


plt.show()
