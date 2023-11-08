import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Parameters for the binomial distribution
n = 20  # Number of trials
p = 0.5  # Probability of success (e.g., coin flip)

# Parameters for the Gaussian distribution (Normal distribution)
mu = n * p  # Mean
sigma = np.sqrt(n * p * (1 - p))  # Standard deviation

# Generate values for the x-axis
x_values = np.arange(0, n+1)

# Calculate the PMF of the binomial distribution
binom_pmf = binom.pmf(x_values, n, p)

# Calculate the PDF of the Gaussian distribution
gaussian_pdf = norm.pdf(x_values, loc=mu, scale=sigma)

# Create a stem plot with connected points
plt.figure(figsize=(10, 6))
plt.stem(x_values, binom_pmf, linefmt='-b', markerfmt='ob', basefmt=" ", label="Binomial PMF")
plt.stem(x_values, gaussian_pdf, linefmt='--r', markerfmt='or', basefmt=" ", label="Gaussian PDF")

# Connect the points with lines
plt.plot(x_values, binom_pmf, '-b', alpha=0.7, label="Connected Binomial PMF")
plt.plot(x_values, gaussian_pdf, '--r', alpha=0.7, label="Connected Gaussian PDF")

# Add labels and legend
plt.xlabel('X')
plt.ylabel('Probability')
plt.title('Binomial PMF vs. Gaussian PDF (Stem Plot with Connected Points)')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

