import numpy as np

print("Assignment 2: Question 10.15.1.12")

# Number of trials to simulate
num_trials = 100000000

# Define the probabilities for each number on the spinner
prob = np.full((8,), 1/8)

# Simulate trials of the spinner
trial_i = np.random.choice(np.arange(1, 9), size=num_trials, p=prob)

# Compute the proportion of times the spinner lands on 8
prob_eight = np.mean(trial_i == 8)
print("Probability of the arrow pointing at 8 is", prob_eight)

# Compute the proportion of times the spinner lands on an odd number
prob_odd = np.mean(trial_i==1) + np.mean(trial_i==3) + np.mean(trial_i==5) + np.mean(trial_i==7)
print("Probability of the arrow pointing at an odd number is", prob_odd)

# Compute the proportion of times the spinner lands on a number greater than 2
prob_gt_2 = np.mean(trial_i > 2)
print("Probability of the arrow pointing at a number greater than 2 is", prob_gt_2)

# Compute the proportion of times the spinner lands on a number less than 9
prob_lt_9 = np.mean(trial_i < 9)
print("Probability of the arrow pointing at a number less than 9 is", prob_lt_9)
