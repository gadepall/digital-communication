import math
import numpy as np
import matplotlib.pyplot as plt


plt.xlabel('k')
plt.ylabel('Pr(A=k)')
Amount = [-6,-3,-1,1.5,4]
Prob = [0.0625,0.25,0.375,0.25,0.0625]
plt.xlim([-7,5])
plt.ylim([0,1])
plt.stem(Amount,Prob)


plt.show()
