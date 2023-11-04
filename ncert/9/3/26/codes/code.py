import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

n = 8  # Number of trials
p = 0.1  # Probability of success

# Parameters for the normal distribution 
mu = n * p
sigma = np.sqrt(n * p * (1 - p))

x = np.arange(0, n+1)

# Compute the PMF of the binomial distribution
binomial_pmf = binom.pmf(x, n, p)

#PDF of the normal distribution
y = np.linspace(0, n, 1000)
normal_pdf = norm.pdf(y, loc=mu, scale=sigma)

# Plot the binomial PMF
plt.stem(x, binomial_pmf, basefmt=" ", markerfmt="bo", linefmt="b-", label='Binomial PMF')

# Plot the normal PDF (approximation)
plt.plot(y, normal_pdf, label='Normal PDF', color='red')

# Add labels and legend
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.legend()

# Show the plot
plt.title('Binomial PMF vs. Normal PDF')
plt.grid(True)
plt.savefig("plot.pdf")
plt.show()
