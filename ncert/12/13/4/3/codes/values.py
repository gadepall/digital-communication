import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import math

#6 Coins are tossed, 1 denotes heads and 0 denotes tails. There are 1000 samples
simlen= 100000

#Probability that heads occurred, i.e., X=1 is 1/2
prob = 0.5

#Generating sample date using Bernoulli r.v.
p1 = bernoulli.rvs(size=simlen,p=prob)
p2 = bernoulli.rvs(size=simlen,p=prob)
p3 = bernoulli.rvs(size=simlen,p=prob)
p4 = bernoulli.rvs(size=simlen,p=prob)
p5 = bernoulli.rvs(size=simlen,p=prob)
p6 = bernoulli.rvs(size=simlen,p=prob)
#Calculating the number of heads
num_heads = p1 + p2 + p3 + p4 + p5 + p6

#calculating the number of tails
num_tails = 6 - num_heads

X1 = num_heads - num_tails
X = abs(X1)

print("Probability through simulation")

print("X: 0 =", np.count_nonzero(X==0)/simlen)
print("X: 2 =", np.count_nonzero(X==2)/simlen)
print("X: 4 =", np.count_nonzero(X==4)/simlen)
print("X: 6 =", np.count_nonzero(X==6)/simlen)

print("Theoretical Probability")
print("X: 0 =", math.comb(6,3)/2**6)
print("X: 2 =", 2*math.comb(6,4)/2**6)
print("X: 4 =", 2*math.comb(6,5)/2**6)
print("X: 6 =", 2*math.comb(6,6)/2**6)


# Generate X1 and X2 without explicit loops
y = np.random.randint(0, 2, size=(6, simlen))

# Calculate X without loops
X = np.sum(y, axis=0)

# Find the frequency of each outcome
unique, counts = np.unique(X, return_counts=True)


# Simulated probability
psim = counts / simlen

actual = []
actual.append(psim[3])
actual.append(psim[2] + psim[4])
actual.append(psim[1] + psim[5])
actual.append(psim[0] + psim[6])
X_axis = [0,2,4,6]

#theoretical probability
Prob = [0.3125,0.46875,0.1875,0.03125]

plt.stem(X_axis, actual, markerfmt='o', linefmt='C0-', use_line_collection=True, label='Simulation')
plt.stem(X_axis, Prob, markerfmt='o', linefmt='C1-', use_line_collection=True, label='Analysis')
plt.xlabel('$k$')  # Use 'k' instead of 'n'
plt.ylabel('$p_{X}(k)$')  # Use 'k' instead of 'n'
plt.legend()
plt.grid()

# Save or display the plot
plt.savefig('/home/aryan/GVV/12.13.4.3/figs/fig.png')


