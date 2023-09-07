#Name: Shaikh Rusna Aiyubbhai
#Roll no.: EE22BTECH11048
#Question 10.13.3.20
import numpy as np

# Simulate throwing two dice a large number of times
num_simulations = 1000000

# Simulate throwing two dice and calculate the probabilities using a vectorized approach
dice1 = np.random.randint(1, 7, (num_simulations,))
dice2 = np.random.randint(1, 7, (num_simulations,))
sum_of_rolls = dice1 + dice2

# Calculate the probabilities for different target sums using vectorized operations
target_sums = np.arange(2, 13)
successful_outcomes = np.sum(sum_of_rolls[:, np.newaxis] == target_sums, axis=0)
probabilities = successful_outcomes / num_simulations

# Calculate the probability of prime sums
prime_sums = np.array([2, 3, 5, 7, 11])
prime_sum_probabilities = np.sum(probabilities[np.isin(target_sums, prime_sums)])

# Calculate the probability of sum 1
prob_sum_1 = np.sum(sum_of_rolls == 1) / num_simulations

# Print the probabilities
print("Probability of sum 7:", probabilities[target_sums == 7][0])
print("Probability of prime sum:", prime_sum_probabilities)
print("Probability of sum 1:", prob_sum_1)

