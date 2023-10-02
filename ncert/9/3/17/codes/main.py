import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Parameters
n = 6  # Number of trials (6 balls drawn)
p_x = 10 / 25  # Probability of drawing X-marked ball
p_y = 15 / 25  # Probability of drawing Y-marked ball

# Values for the x-axis (number of X-marked balls)
x_values = np.arange(0, n + 1)

# Calculate the PMF of the binomial distribution for each x
binomial_pmf_x = binom.pmf(x_values, n, p_x)
binomial_pmf_y = binom.pmf(x_values, n, p_y)

# Parameters for the Gaussian distribution (normal approximation)
mu_x = n * p_x
sigma_x = np.sqrt(n * p_x * (1 - p_x))
mu_y = n * p_y
sigma_y = np.sqrt(n * p_y * (1 - p_y))

# Values for the x-axis for the Gaussian distribution
x_gaussian = np.linspace(0, n, 1000)
pdf_gaussian_x = norm.pdf(x_gaussian, loc=mu_x, scale=sigma_x)
pdf_gaussian_y = norm.pdf(x_gaussian, loc=mu_y, scale=sigma_y)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the PMF of the binomial distribution for X and Y
ax.stem(x_values, binomial_pmf_x, basefmt=' ', linefmt='b-', markerfmt='bo', label='Binomial PMF (X)')
ax.stem(x_values, binomial_pmf_y, basefmt=' ', linefmt='g-', markerfmt='go', label='Binomial PMF (Y)')

# Plot the PDF of the Gaussian distribution for X and Y
ax.plot(x_gaussian, pdf_gaussian_x, label='Gaussian PDF (X)', color='red')
ax.plot(x_gaussian, pdf_gaussian_y, label='Gaussian PDF (Y)', color='purple')

# Set labels and title
ax.set_xlabel('Number of Balls Marked')
ax.set_ylabel('Probability')
ax.set_title('Probability Distributions for X and Y Marked Balls')

# Add a legend
ax.legend()

# Show the plot
plt.grid(True)
plt.show()

# Calculate and print the specific probabilities
probability_all_X = binomial_pmf_x[n]
probability_not_more_than_2_Y = np.sum(binomial_pmf_y[:3])
probability_at_least_one_Y = 1 - binomial_pmf_y[0]
probability_equal_X_and_Y = binomial_pmf_x[int(n / 2)]

print(f"Probability that all balls drawn will bear the X mark: {probability_all_X:.4f}")
print(f"Probability that not more than 2 balls will bear the Y mark: {probability_not_more_than_2_Y:.4f}")
print(f"Probability that at least one ball will bear the Y mark: {probability_at_least_one_Y:.4f}")
print(f"Probability that the number of X-marked balls equals the number of Y-marked balls: {probability_equal_X_and_Y:.4f}")

