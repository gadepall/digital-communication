import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Gaussian Distribution
mu = 3
sigma = np.sqrt(1.5)

x = np.arange(7)
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

print("Gaussian Probability values:")
print("x =        ",x)
print("P(x = x) = ",y)

