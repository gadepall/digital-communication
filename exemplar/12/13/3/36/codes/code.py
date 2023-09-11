import numpy as np
from scipy.optimize import fsolve

# Define the equation to find p
def equation(p):
    # Calculate E(X) and E(X^2)
    expected_x = (0 * p) + (1 * p) + (2 * (1 - 2 * p))
    expected_x_squared = (0**2 * p) + (1**2 * p) + (2**2 * (1 - 2 * p))
    # Equate E(X) and E(X^2)
    return expected_x - expected_x_squared

# Solve for p
p_solution = fsolve(equation, 0.5)[0]

# Print the solution for p
print(f"The value of p is approximately {p_solution:.4f}")

# Simulate the random variable X with the calculated p
num_simulations = 100000
X_simulated = np.random.choice([0, 1, 2], num_simulations, p=[p_solution, p_solution, 1 - 2 * p_solution])

# Calculate the average value of the simulated X
average_simulated_x = np.mean(X_simulated)

# Verify the calculated p with simulation
print(f"Average simulated X: {average_simulated_x:.4f}")

