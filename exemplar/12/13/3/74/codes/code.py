#Theory

import numpy as np
from scipy.special import comb
#There are three cases to draw exactly one red balls without replacement
#So probability of one red bal is given by
total_balls = 8  # 5 red + 3 blue
# Number of ways to choose 3 balls out of 8
total_ways = comb(total_balls, 3, exact=True)
# Number of ways to choose 1 red and 2 blue balls
ways_one_red = comb(5, 1, exact=True) * comb(3, 2, exact=True)
# Probability of getting exactly one red ball
prob_theory= ways_one_red / total_ways
print(f"theoritical probability = {round(prob_theory,3)}")



#Simulation

num_simulations = 1000
# Simulate drawing 3 balls num_simulations times with replacement
simulated_draws = np.random.choice(total_balls, size=(num_simulations, 3), replace=True)
# Count the number of sets where exactly one red ball is drawn
count_one_red = np.sum(np.sum(simulated_draws == 0, axis=1) == 1)
prob_simulation= count_one_red / num_simulations
print(f"Simulated probability = {prob_simulation}")
