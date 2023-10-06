import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Parameters for the binomial distribution
n = 7  # Number of trials
p = 0.25  # Probability of success in a single trial

# Parameters for the Gaussian approximation
mu = n * p
sigma = np.sqrt(n * p * (1 - p))

# Generate a higher-resolution set of x-values for a smoother curve
x_values = np.linspace(0, n, 1000)

# Calculate PMF (binomial distribution)
pmf_values = binom.pmf(np.arange(0, n + 1), n, p)

# Calculate PDF (Gaussian approximation) for the higher-resolution x-values
pdf_values = norm.pdf(x_values, loc=mu, scale=sigma)

# Plot PMF (binomial distribution) as a stem plot
plt.stem(np.arange(0, n + 1), pmf_values, basefmt=' ', label='Binomial PMF', use_line_collection=True, markerfmt='ro')

# Plot PDF (Gaussian approximation) as a smooth line
plt.plot(x_values, pdf_values, label='Gaussian PDF', color='blue')

# Set labels and title
plt.xlabel('Number of Successful Shots (X)')
plt.ylabel('Probability')
plt.title('PMF and PDF for Number of Successful Shots')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

