import random
import numpy as np

def probability_of_53_sundays():
    days_in_week = 7
    return 1 / days_in_week

def bernoulli_trial(probability, num_simulations):
    random_numbers = np.random.random(num_simulations)
    return np.sum(random_numbers < probability)

num_simulations = 10000
prob = probability_of_53_sundays()

num_53_sundays = bernoulli_trial(prob, num_simulations)
simulated_prob = num_53_sundays / num_simulations

print(f"Simulated probability of getting 53 Sundays in a non-leap year: {simulated_prob:.2f}")
