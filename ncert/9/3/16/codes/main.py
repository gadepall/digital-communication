import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Parameters for the binomial distribution
n = 10  # random sample
p = 0.9 # Probability of right-handed people

# Parameters for the normal distribution (approximation to binomial)
mu = n * p
sigma = np.sqrt(n * p * (1 - p))

# Generate values for x (number of right-handed people in binomial)
x = np.arange(0, n+1)

# Compute the PMF of the binomial distribution
binomial_pmf = binom.pmf(x, n, p)
binomial_req = sum(binomial_pmf[:7])
print(f"The probability that atmost 6 out of 10 are right- handed (Binomial):{binomial_req}") 

# Generate values for y (PDF of the normal distribution)
y = np.linspace(0, n, 1000)
gaussian_pdf = norm.pdf(y, loc=mu, scale=sigma)
gaussian_req_without_correction = norm.pdf(6, loc=mu, scale=sigma)
gaussian_req_with_correction = norm.pdf(6.5, loc=mu, scale=sigma)
print(f"The probability that atmost 6 out of 10 are right- handed (Gaussian without correction):{gaussian_req_without_correction}") 
print(f"The probability that atmost 6 out of 10 are right- handed (Gaussian with correction):{gaussian_req_with_correction}") 

# Plot the binomial PMF
plt.stem(x, binomial_pmf, basefmt=" ", markerfmt="bo", linefmt="b-", label='Binomial PMF')

# Plot the normal PDF (approximation)
plt.plot(y, gaussian_pdf, label='Gaussian PDF', color='red')

# Add labels and legend
plt.xlabel('Number of Right-handed people')
plt.ylabel('Probability / Probability Density')
plt.legend()

# Show the plot
plt.title('Binomial PMF vs. Gaussian PDF')
plt.grid(True)
plt.savefig("../figs/fig.png")
plt.show()
