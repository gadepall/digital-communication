import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Sample size
simlen = 100000
# Possible outcomes
k_values = np.arange(3, 19)

# Generate X1 and X2 without explicit loops
y = np.random.randint(1, 7, size=(3, simlen))

# Calculate X without loops
X = np.sum(y, axis=0)

# Find the frequency of each outcome
unique, counts = np.unique(X, return_counts=True)

# Simulated probability
psim = counts / simlen #Prob of sum 6 is psim[3]

Z = np.all(y == 2, axis=0)
uniqueZ, countsZ = np.unique(Z, return_counts=True)

psimZ = countsZ/simlen #Prob of all 2 is psimZ[1] 

print(psimZ[1]/psim[3]) 

#Theoretical Probability
p_X3 = 1/216
p_Y6 = 10/216
p_X3andY5 = 1/216
p_X3givenY6 = p_X3andY5/p_Y6
print(p_X3givenY6)

# Plotting
plt.stem(k_values, psim, markerfmt='o', linefmt='C0-', use_line_collection=True, label='Simulation')
plt.xlabel('$k$')  # Use 'k' instead of 'n'
plt.ylabel('$p_{X}(k)$')  # Use 'k' instead of 'n'
plt.legend()
plt.grid()

# Save or display the plot
plt.show()

