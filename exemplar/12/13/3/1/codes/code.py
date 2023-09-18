import numpy as np
import matplotlib.pyplot as plt

# Define the probability distribution for the loaded die
loaded_die_probs = [0.2, 0.2, 0.1, 0.3, 0.1, 0.1]  

# Simulate rolling the loaded die twice
num_rolls = 10000  # You can adjust the number of rolls as needed
X = np.random.choice(np.arange(1, 7), num_rolls, p=loaded_die_probs)
Y = np.random.choice(np.arange(1, 7), num_rolls, p=loaded_die_probs)

# Calculate Z as the sum of X and Y
Z = X + Y
W = X - Y

# Calculate the probabilities for each value of W
unique_values, counts = np.unique(W, return_counts=True)
probabilities = counts / num_rolls

# Create a stem plot
plt.figure(figsize=(8, 6))
plt.stem(np.unique(Z), np.bincount(Z)[np.unique(Z)] / num_rolls, markerfmt='ro', basefmt=' ', linefmt='k-')
plt.title('Stem Plot of Z = X + Y (Two Rolls of Loaded Die)')
plt.xlabel('Z (Sum of X and Y)')
plt.ylabel('Probability')
plt.xticks(np.arange(2, 13))
plt.grid(True)
plt.savefig('../figs/Z.png')

plt.figure(figsize=(8, 6))
plt.stem(unique_values, probabilities, markerfmt='ro', basefmt=' ', linefmt='k-')
plt.title('Stem Plot of W = X - Y (Two Rolls of Loaded Die)')
plt.xlabel('W (Difference between X and Y)')
plt.ylabel('Probability')
plt.xticks(np.arange(-5, 6))
plt.grid(True)
plt.savefig('../figs/W.png')

