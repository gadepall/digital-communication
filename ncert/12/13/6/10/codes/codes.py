import math
import numpy as np
from scipy.stats import bernoulli

def calculate_num_tosses(target_probability):
    # Using the formula to calculate the number of tosses needed
    p = 0.5  # Probability of success (getting a head) for a fair coin toss
    q = 1 - p  # Probability of failure (getting a tail)
    num_tosses = math.ceil(math.log(1 - target_probability, q))
    return num_tosses

target_probability = 0.9  # Desired probability of success (getting at least one head)
num_tosses_needed = calculate_num_tosses(target_probability)

print(f"Number of coin tosses needed to exceed {target_probability*100}% probability: {num_tosses_needed}")

# Simulating Bernoulli trials with probability p for a fair coin toss

data_bern = bernoulli.rvs(size=100000, p=target_probability)
err_ind = np.nonzero(data_bern == 1)
probability_simulation = np.size(err_ind) / 100000
print("Probability-simulation, actual:", probability_simulation)

