import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom


# Dataset
n=5
p=0.05
simlen = 10000000
q=0.95
data_binom = binom.rvs(n,p,size=simlen)
x, y = np.unique(data_binom, return_counts= True)
# while np.size(x) < 6:
#     x = np.append(x , x[np.size(x) -1] + 1)
# while np.size(y) < 6:
#     y = np.append(y , 0)

y = np.cumsum(y)/simlen

actual = np.array(binom.cdf(x, n , p))

# Plotting the Graph
plt.figure(figsize = (18 , 12))
plt.stem(x, y ,markerfmt = 'go' , linefmt = 'r-' , label = 'Observation')
plt.ylim(0 , 1.2)
plt.xlim(-0.5 , 6)
plt.title("Curve plotted using the given points")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(np.arange(0 , 6) , actual , 'yo' , label = 'Theoretical')
plt.legend()
plt.show()