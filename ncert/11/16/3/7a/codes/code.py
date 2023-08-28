import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Generating vectors of successes
x1 = np.random.randint(0, 2, size=10000)
x2 = np.random.randint(0, 2, size=10000)
x3 = np.random.randint(0, 2, size=10000)
x4 = np.random.randint(0, 2, size=10000)

# Calculate successful outcomes
successful_outcomes = x1 + x2 + x3 + x4

# Count occurrences of each outcome
counts = np.bincount(successful_outcomes, minlength=5)

# Define possible values of h
possible_values_of_h = np.arange(0, 5)

# Calculate total money based on outcomes
total_money = possible_values_of_h * 1 + (possible_values_of_h - 4) * 1.5

# Calculate probabilities
probabilities = counts / 10000

# Print results
print("Total Money:", *map(lambda x: f"{x:.2f}", total_money))
print("Probability:", *map(lambda x: f"{x:.4f}", probabilities))

#for plotting and simulation
# Sample size
simlen = 10000

# Possible outcomes
k_values = np.arange(0, 5)


# Generate X1 and X2 without explicit loops
y = np.random.randint(0, 2, size=(4, simlen))

# Calculate X without loops
X = np.sum(y, axis=0)

# Find the frequency of each outcome
unique, counts = np.unique(X, return_counts=True)

# Simulated probability
psim = counts / simlen

X_axis = [4,1.5,-1,-3.5,-6]

#Theoretical Probability
Prob = [0.0625,0.25,0.375,0.25,0.0625]


# Plotting
plt.stem(X_axis, psim, markerfmt='o', linefmt='C0-', use_line_collection=True, label='Simulation')
plt.stem(X_axis, Prob, markerfmt='o', linefmt='C1-', use_line_collection=True, label='Analysis')
plt.xlabel('$A$')  # Use 'k' instead of 'n'
plt.ylabel('$p_{A}(k)$')  # Use 'k' instead of 'n'
plt.legend()
plt.grid()

# Save or display the plot
plt.savefig('/home/dhruv/EE23010/Assignment2/figs/figure1.png')
plt.show()

