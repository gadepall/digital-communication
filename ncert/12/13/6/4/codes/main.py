import scipy.stats as stats
import numpy as np

# Parameters
probability_right_handed = 0.9  # Probability of being right-handed
sample_size = 10  # Size of the random sample

# Simulate the Bernoulli trials for the sample
def simulate_bernoulli(sample_size, p, num_simulations):
    bernoulli_results = stats.bernoulli.rvs(p, size=(num_simulations, sample_size))
    return bernoulli_results

# Calculate the simulated probability of at most 6 right-handed individuals using Bernoulli trials
def simulated_probability_at_most_6(bernoulli_results):
    successes_at_most_6 = np.sum(bernoulli_results, axis=1) <= 6
    prob_at_most_6 = np.mean(successes_at_most_6)
    return prob_at_most_6

# Calculate the theoretical probability using the Binomial distribution
def theoretical_probability_at_most_6(sample_size, p):
    binom_dist = stats.binom(sample_size, p)
    prob = binom_dist.cdf(6)
    return prob

# Simulate Bernoulli trials
num_simulations = 100000
bernoulli_results = simulate_bernoulli(sample_size, probability_right_handed, num_simulations)

# Calculate simulated probability
simulated_prob = simulated_probability_at_most_6(bernoulli_results)

# Calculate theoretical probability
theoretical_prob = theoretical_probability_at_most_6(sample_size, probability_right_handed)

# Print the results
print("Simulated Probability (at most 6):", simulated_prob)
print("Theoretical Probability (at most 6):", theoretical_prob)


