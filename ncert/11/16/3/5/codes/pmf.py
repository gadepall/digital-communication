import matplotlib.pyplot as plt
import numpy as np

# Define the pmf of tossing a coin
coin_pmf = np.array([1/2, 0, 0, 0, 0, 1/2])

# Define the pmf of rolling a die
die_pmf = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

# Convolve the two pmfs
convolved_pmf = np.convolve(coin_pmf, die_pmf)

# Define the possible values of the sum
sum_values = np.arange(2, 13)

# Plot the convolved pmf as a stem plot
fig, ax = plt.subplots()
ax.stem(sum_values, convolved_pmf[:len(sum_values)], use_line_collection=True)

# Set the axis labels and title
ax.set_xlabel('Sum of Coin and Die')
ax.set_ylabel('Probability')
ax.set_title('PMF of Sum of Coin and Die')

# Set the x-axis ticks and tick labels
ax.set_xticks(sum_values)
ax.set_xticklabels(sum_values)

# Set the y-axis limit
ax.set_ylim(0, 1/4)

# Display the plot
plt.show()


