import math
import numpy as np
import matplotlib.pyplot as plt


plt.xlabel('k')
plt.ylabel('Pr(X<=k)')
heads = [0,1,2,3,4,5]
Prob = [0.0625,0.25,0.375,0.25,0.0625,0]
cdf_X=np.cumsum(Prob)
plt.stem(heads,cdf_X)
plt.xlim([-1,6])
plt.ylim([0,1.1])


plt.show()
