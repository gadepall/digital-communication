import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom

simlen=10000000
n=6
p=0.5
q=0.5

data_binom = binom.rvs(n,p,size=simlen)
x, y = np.unique(data_binom, return_counts= True)

y = np.cumsum(y)/simlen

actual = np.array(binom.cdf(x, n , p))

plt.figure(figsize = (18 , 12))
plt.stem(x, y ,markerfmt = 'go' , linefmt = 'r-' , label = 'Observation')
plt.ylim(0 , 1.2)
plt.xlim(-0.5 , 6)
plt.title("Curve plotted using the given points")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(np.arange(0 , 7) , actual , 'yo' , label = 'Theoretical')
plt.legend()
plt.show()
