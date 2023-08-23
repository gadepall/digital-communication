import numpy as np
import scipy.stats as stats
p = 0.5  # Probability of success
bernoulli_dist = stats.bernoulli(p)
num_trials = 20
trial_outcomes = bernoulli_dist.rvs(size=num_trials)
x = 12
required_probability = 1 - bernoulli_dist.cdf(x - 1)
print("Trial outcomes:", trial_outcomes)
print("Probability of more than 12 successes:", required_probability)

