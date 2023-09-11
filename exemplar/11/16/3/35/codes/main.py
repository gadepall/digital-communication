import numpy as np

# Number of trials for the simulation
num_trials = 100000

# Simulate events A and B (generate random numbers between 0 and 1)
random_numbers_A = np.random.rand(num_trials)
random_numbers_B = np.random.rand(num_trials)

# Define probabilities
P_A = 0.7
P_B = 0.3
P_A_and_B = 0.4

# Simulate events based on probabilities
events_A = random_numbers_A <= P_A
events_B = random_numbers_B <= P_B

# Calculate empirical probabilities
empirical_P_A = np.mean(events_A)
empirical_P_B = np.mean(events_B)

# Calculate the probability of A and B occurring together
events_A_and_B = events_A & events_B
empirical_P_A_and_B = np.mean(events_A_and_B)

# Check if the empirical probabilities match the given probabilities
consistent = (
    round(empirical_P_A, 1) == P_A
    and round(empirical_P_B, 1) == P_B
    and round(empirical_P_A_and_B, 1) == P_A_and_B
)

if consistent:
    print("The statement is consistent with the simulation.")
else:
    print("The statement is not consistent with the simulation.")

# Print the empirical probabilities for reference
print(f"Empirical P(A): {empirical_P_A:.4f}")
print(f"Empirical P(B): {empirical_P_B:.4f}")
print(f"Empirical P(A and B): {empirical_P_A_and_B:.4f}")
