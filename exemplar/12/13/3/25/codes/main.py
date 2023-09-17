import numpy as np
import matplotlib.pyplot as plt
import random as rand

# np.set_printoptions(threshold=np.inf)

# Using dice rolls
n =10000
choices = [0,1,2,3]
weights = [0.5333,0.2667,0.1333,0.0667]
def dice_roll():
	dice = np.array(rand.choices(choices, weights,k=n))         
	return dice
X = dice_roll()
values, sim_count = np.unique(X, return_counts=True)
pmf_sum_sim = np.array(sim_count)/n
x = np.arange(0,5)
y = np.arange(0,1)
print("value =",values,"\n","probability =",pmf_sum_sim,"\nTheoretical =",weights)
cdf_sum_sim = np.cumsum(pmf_sum_sim)
cdf_sum_thr = np.cumsum(weights)
plt.stem(choices, weights, linefmt='b-', markerfmt='bo')
plt.stem(values, pmf_sum_sim, linefmt='none', markerfmt='go')
plt.xlabel('X')
plt.ylabel('P(X)')
plt.title("PMF of X")
plt.legend(['Theoretical', 'Simulated'])
plt.savefig('/home/lancelot/Latex/EE2102/12.13.3.25/figs/pmf.png')
plt.show()

plt.stem(choices, cdf_sum_thr, linefmt='b-', markerfmt='bo')
plt.stem(values, cdf_sum_sim, linefmt='none', markerfmt='go')
plt.xlabel('X')
plt.ylabel('F(X)')
plt.title("CDF of X")
plt.legend(['Theoretical', 'Simulated'])
plt.savefig('/home/lancelot/Latex/EE2102/12.13.3.25/figs/cdf.png')
plt.show()
