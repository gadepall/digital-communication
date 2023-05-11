import numpy as np
import matplotlib.pyplot as plt

# Define the sample space of the spinner
sample_space = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Define the probability distribution of the spinner

prob_dist = [0, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8]

# Calculate the cumulative probabilities for the spinner

cumulative_prob = np.cumsum(prob_dist)

# Plot the CDF using a stem plot

plt.stem(cumulative_prob)
plt.title ("Cumulative Distribution Function for the Spinner")
plt.xlabel("Observation")
plt.ylabel (" Cumulative Probability")
plt.grid('on' 'on')
plt.show()
plt.savefig("../figs/cdf.png")