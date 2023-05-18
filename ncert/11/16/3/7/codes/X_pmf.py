import math
import numpy as np
import matplotlib.pyplot as plt


plt.xlabel('k')
plt.ylabel('Pr(X=k)')
heads = [0,1,2,3,4]
Prob = [0.0625,0.25,0.375,0.25,0.0625]
plt.xlim([-1,5])
plt.ylim([0,1])
plt.stem(heads,Prob)


plt.show()
