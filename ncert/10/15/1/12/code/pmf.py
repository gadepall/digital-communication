import numpy as np
import matplotlib.pyplot as plt

# Define the sample space of the spinner
sample_space = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Define the probability distribution of the spinner

prob_dist = [0, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8]

# Define the pmf for the spinner

pmf = [0, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8]

# Plot the PMF using a stem plot

plt.stem(pmf)
plt.title ("Probability Mass Function for the Spinner")
plt.xlabel("Observation")
plt.ylabel ("PMF")
plt.grid('on' 'on')
plt.show()
plt.savefig("../figs/pmf.png")