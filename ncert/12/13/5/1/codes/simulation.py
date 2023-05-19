
import numpy as np

def throw_die():
    return np.random.randint(1, 7)

def simulate_trials(num_trials):
    throws = np.random.randint(1, 7, size=(num_trials, 6))
    odd_counts = np.sum(throws % 2 != 0, axis=1)
    successes = np.count_nonzero(odd_counts == 5)
    return successes / num_trials

# Probability of 5 successes
num_trials = 1000000
prob_5_successes = simulate_trials(num_trials)
print(f"Probability of 5 successes: {prob_5_successes}")

# Probability of at least 5 successes
throws = np.random.randint(1, 7, size=(num_trials, 6))
odd_counts = np.sum(throws % 2 != 0, axis=1)
success_count = np.count_nonzero(odd_counts >= 5)
prob_at_least_5_successes = success_count / num_trials
print(f"Probability of at least 5 successes: {prob_at_least_5_successes}")

# Probability of at most 5 successes
success_count = np.count_nonzero(odd_counts <= 5)
prob_at_most_5_successes = success_count / num_trials
print(f"Probability of at most 5 successes: {prob_at_most_5_successes}")


