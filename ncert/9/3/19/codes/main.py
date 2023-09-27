import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Sample size
simlen = 10000

# Possible outcomes
k_values = np.arange(0, 7)

# Generate X1 and X2 without explicit loops
y = np.random.randint(0, 2, size=(6, simlen))

# Calculate X without loops
X = np.sum(y, axis=0)

# Find the frequency of each outcome
unique, counts = np.unique(X, return_counts=True)

# Simulated probability
psim = counts / simlen

#Theoretical Probability
p = 0.5 
n = 6

#We can use binom to create binomial distribution
rv = binom(n, p)

#Make the list combinations with rv.pmf function
combinations = rv.pmf(k_values)

# Find the most likely outcome
most_likely_outcome = np.argmax(combinations)

print(f"Therefore the most likely outcome is for X = {most_likely_outcome}")

# Gaussian Distribution
mu = 3
sigma = np.sqrt(1.5)

x = np.linspace(0, 6, 100)
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)


# Plotting
plt.stem(k_values, combinations, markerfmt='blue', linefmt='blue',  label='Binomial Distribution')
plt.plot(x, y, color='green', linestyle='-', linewidth=1, label = 'Gaussian Curve')
plt.xlabel('$k$')  # Use 'k' instead of 'n'
plt.ylabel('$p_{X}(k)$')  # Use 'k' instead of 'n'
plt.legend()
plt.grid()
plt.show()
