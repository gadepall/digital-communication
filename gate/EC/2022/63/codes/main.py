import scipy.integrate as spi
import numpy as np

# Define the conditional probability density functions
def fY_given_xA(y):
  return np.exp(-(y+1))

def fY_given_xB(y):
  return np.exp(y-1) * (1 - (y < -1))

# Define the intervals for integration
interval_xA = (0, 1)
interval_xB = (-1, 0)

# Calculate the total probability of error
Pe = 0.5 * spi.quad(fY_given_xA, *interval_xA)[0] + 0.5 * spi.quad(fY_given_xB, *interval_xB)[0]


# Define a function to generate Y
def generate_Y(num_samples):
    u = np.random.rand(num_samples)
    y_xA = -1 - np.log(1 - u)
    y_xB = 1 + np.log(u)
    transmitted_symbols = np.random.choice([-1, 1], size=num_samples, p=[0.5, 0.5])
    y = np.where(transmitted_symbols == -1, y_xA, y_xB)
    return y

# Obtain the empirical probability of error
num_samples = 10000
Y_samples = generate_Y(num_samples)

# Calculate the number of errors
errors = np.sum(np.abs(Y_samples) > 1)

# Calculate the empirical probability of error
Pe_empirical = errors / num_samples

print(f"Empirical Probability of Error (Pe): {Pe_empirical}")

