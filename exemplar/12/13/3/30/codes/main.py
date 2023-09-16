import numpy as np

# Define the probability distributions for X and Y
px = np.array([1/5, 2/5, 1/5, 1/5])
py = np.array([1/5, 3/10, 2/5, 1/10])

# Calculate E(Y^2) without a for loop using NumPy
ey2 = np.sum((np.arange(len(py)) ** 2) * py)

# Calculate E(X) without a for loop using NumPy
ex = np.sum(np.arange(len(px)) * px)

print("E(Y^2):", ey2)
print("E(X):", ex)

# Check if E(Y^2) equals 2 * E(X)
if ey2 == 2 * ex:
    print("E(Y^2) = 2 * E(X), hence proved.")
else:
    print("E(Y^2) is not equal to 2 * E(X), the equality does not hold.")

