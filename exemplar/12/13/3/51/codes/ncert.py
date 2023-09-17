import random
import numpy as np

# Numbers and weights
nums = np.arange(1,7)
pr = np.concatenate(([np.arange(1,4)**2],[np.arange(4,7)*2])).flatten()

# Generating 10000 random numbers with given probability weights
random_numbers = np.array(random.choices(nums, weights = pr, k = 10000))

# Expeected values
ex = sum(random_numbers)/10000
e3x2 = sum(3*np.multiply(random_numbers,random_numbers))/10000
pgeq4 = (random_numbers >= 4).sum()/10000

# Output
print("E(X) =      ",ex)
print("E(3X^2) =   ",e3x2)
print("P(X >= 4) = ",pgeq4)