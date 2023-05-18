import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom

x = [4,3,2,1,0]

y = [4,1.5,-1,-3.5,-6]
 
plt.stem(x, y)

plt.xlabel('No. of heads')

plt.ylabel('Amount')

plt.title('Amount gained/lost')
plt.show()
