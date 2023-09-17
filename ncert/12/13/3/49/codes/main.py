import numpy as np

# Define the probability mass function
def pmf(x, k):
    return np.where(np.isin(x, [1, 2, 3, 4]), k * (x + 1), np.where(np.isin(x, [5, 6, 7]), 2 * k * x, 0))

# Define the range of possible values for X
x_values = np.arange(1, 8)

# Define the equations for E(X) and Var(X)
def expected_value(k):
    return np.sum(x_values * pmf(x_values, k))

def variance(k):
    return np.sum((x_values - expected_value(k))**2 * pmf(x_values, k))

# (i) Solve for k
def calculate_k():
    k_candidates = np.linspace(0.001, 10, 10000)
    eq_values = np.sum(pmf(x_values, k_candidates[:, np.newaxis]), axis=1) - 1
    k_index = np.argmin(np.abs(eq_values))
    return k_candidates[k_index]

# Perform 10,000 simulations
num_simulations = 10000

# Calculate k values
k_values = np.array([calculate_k() for _ in range(num_simulations)])

# Calculate expected values and variances
expected_x_values = np.array([expected_value(k) for k in k_values])
variance_values = np.array([variance(k) for k in k_values])

# Calculate averages
avg_k = np.mean(k_values)
avg_expected_x = np.mean(expected_x_values)
avg_std_dev_x = np.mean(np.sqrt(variance_values))

# Print the results
print(f"Avg. Value of k: {avg_k}")
print(f"Avg. E(X): {avg_expected_x}")
print(f"Avg. Standard Deviation of X: {avg_std_dev_x}")

