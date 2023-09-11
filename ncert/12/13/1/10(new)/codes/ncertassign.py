import numpy as np

# Number of simulations
num_simulations = 1000000

# Simulate rolling two dice
black_die = np.random.randint(1, 7, num_simulations)
red_die = np.random.randint(1, 7, num_simulations)

# (a) Calculate the conditional probability of sum greater than 9 given black die is 5
condition_a = (black_die == 5)
num_cases_a = np.sum((black_die + red_die > 9) & condition_a)
total_cases_a = np.sum(condition_a)
sum_greater_than_9_given_black_5 = num_cases_a / total_cases_a

# (b) Calculate the conditional probability of sum 8 given red die is less than 4
condition_b = (red_die < 4)
num_cases_b = np.sum((black_die + red_die == 8) & condition_b)
total_cases_b = np.sum(condition_b)
sum_8_given_red_less_than_4 = num_cases_b / total_cases_b

print("Conditional probability of obtaining sum > 9 given black die is 5:", sum_greater_than_9_given_black_5)
print("Conditional probability of obtaining sum 8 given red die is < 4:", sum_8_given_red_less_than_4)
