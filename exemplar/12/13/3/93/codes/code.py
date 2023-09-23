import numpy as np
from scipy.stats import bernoulli

# Parameters
total_pens = 100
defective_pens = 10
sample_size = 5
num_simulations = 100000

# Calculate the probability of drawing a defective pen
p_defective = defective_pens / total_pens

# Theoretical calculation using the Bernoulli distribution
# Probability of 0 defective pens
prob_0_defective = (1 - p_defective) ** sample_size

# Probability of 1 defective pen
prob_1_defective = sample_size * p_defective * (1 - p_defective) ** (sample_size - 1)

# Probability of at most 1 defective pen
prob_at_most_1_defective = prob_0_defective + prob_1_defective

# Simulation
simulated_results = np.random.choice([0, 1], size=(num_simulations, sample_size), p=[1 - p_defective, p_defective])
simulated_at_most_1_defective = np.sum(simulated_results, axis=1) <= 1
simulated_prob = np.mean(simulated_at_most_1_defective)

# Print results
print("Theoretical Probability (at most 1 defective):", prob_at_most_1_defective)
print("Simulated Probability (at most 1 defective):", simulated_prob)

