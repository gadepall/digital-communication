import matplotlib.pyplot as plt
import numpy as np

def pmf(k):
    n = 5
    p = 0.1
    return np.math.comb(n, k) * p**k * (1-p)**(n-k)
    
x = np.arange(6)
    
# Set up the plot
fig, ax = plt.subplots()

# Plot the PMF as a vertical line at each possible value of X
for i in range(len(x)):
    ax.vlines(x[i], 0, pmf(x[i]), color=(0, 0, 0.5) , linestyles='solid', linewidth=2)
    plt.plot(x[i], pmf(x[i]),'bo',color=(0, 0, 0.5) )
    
# Set the x-axis label and title of the plot
ax.set_xlabel('$X$', fontsize=16)
ax.set_ylabel('PMF', fontsize=16)

#Save and Display the plot
plt.savefig("../figs/pmf_plot.pdf")
plt.show()

