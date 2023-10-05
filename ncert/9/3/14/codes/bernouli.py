from scipy.stats import norm
from scipy.stats import binom
import numpy as np
from matplotlib import pyplot as plt

# Parameters
p = 1/3  # Probability of success (correct answer)
n = 5    # Number of trials (questions)
k = 4    # Number of successes (correct answers)

# Calculate z-score with the corrected formula
a = (k + 0.5)-(n * p) -1
b = np.sqrt(n * p * (1 - p))
z =a/1.05 #(z score)
print("a",a)
# Calculate and print the probability from Gaussian approximation
prob_gaussian = 1 - norm.cdf(abs(z))
print("Probability from Gaussian approximation: ", prob_gaussian)
print("z",z)
# Calculate and print the probability from Binomial distribution
prob_binomial = 1 - binom.cdf(k - 1, n, p)  # Using cumulative probability
print("Probability from Binomial: ", prob_binomial)

# Create a plot to compare the Gaussian and Binomial distributions
n = 5
p = 1/3
sig = np.sqrt(n * p * (1 - p))
k = np.linspace(0, n, n + 1)
fig, ax = plt.subplots()
xpoints = k
ypoints = np.array(binom.pmf(k, n, p))
ax.stem(xpoints, ypoints, linefmt='r-', markerfmt='ro', basefmt='k--')
xpoints = np.linspace(-n, n, 100 * n)
ypoints = np.array(norm(n * p, sig).pdf(xpoints))
ax.plot(xpoints, ypoints, 'b')
plt.legend(["Gaussian", "Binomial"])
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.grid()
plt.show()

