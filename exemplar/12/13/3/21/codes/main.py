import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom
from scipy.stats import bernoulli
n = 10  # Number of coin tosses
p = 0.5  # Probability of getting a head

x = np.arange(0, n+1)
pmf_values = binom.pmf(x, n, p)
plt.stem(x, pmf_values)
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('PMF of Number of Heads in Two Coin Tosses')
plt.xticks(x)
plt.grid(True)
plt.show()

cdf_values = binom.cdf(x, n, p)
plt.figure(1)
plt.plot(x, cdf_values, marker='o', linestyle='-', drawstyle='steps-post')
plt.xlabel('Number of Heads')
plt.ylabel('Cumulative Probability')
plt.title('CDF of Number of Heads in Two Coin Tosses')
plt.xticks(x)
plt.grid(True)
plt.savefig('/home/sujalgupat484/Desktop/probability/21/figs/figure2.png')


simlen=int(1000000)

#Probability of the event
prob = 0.5

#Generating sample date using Bernoulli r.v.
data_bern = bernoulli.rvs(p=prob,size=(n,simlen))
#Calculating the number of favourable outcomes
err_ind = np.nonzero(data_bern == 1)
#calculating the probability
err_n = np.size(err_ind)/simlen


temp = np.array(data_bern)
add=temp.sum(axis=0)

# Count occurrences of each outcome
counts = np.bincount(add, minlength=10)

# Calculate probabilities
probabilities = counts / 10000
# Possible outcomes
k_values = np.arange(0, 11)
# # Find the frequency of each outcome
# unique, counts = np.unique(X, return_counts=True)

# Simulated probability
psim = counts / simlen

X_axis = x = np.arange(0, n+1)
# Plotting
plt.figure(2)
plt.stem(X_axis, psim, label='Simulation',linefmt='blue')
plt.stem(X_axis, pmf_values, label='Analysis',linefmt='orange')
plt.xlabel('$A$')  # Use 'k' instead of 'n'
plt.ylabel('$p_{A}(k)$')  # Use 'k' instead of 'n'
plt.legend()
plt.title('Comaprision of theoretical and calculated PMF values')
plt.grid()
plt.savefig('/home/sujalgupat484/Desktop/probability/21/figs/figure1.png')


count = np.count_nonzero(add>=8)
print("simulated prob of getting atleast 8 heads ", count/simlen)
