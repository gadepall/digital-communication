import numpy as np

# Generate a shuffled list of numbers from 1 to 1000
numbers = np.arange(1, 1001)
np.random.shuffle(numbers)

# Find the perfect squares greater than 500 without loops
mask_gt_500 = numbers > 500
is_perfect_square = (np.sqrt(numbers) % 1 == 0)
perfect_squares_gt_500 = numbers[mask_gt_500 & is_perfect_square]

# Count the occurrences of perfect squares greater than 500
count_prizes = np.sum(mask_gt_500 & is_perfect_square)

# Total number of simulations
total_simulations = len(numbers)

# Probability calculation
probability_first_player = count_prizes / total_simulations

# After the first player wins, remove their card from the list
numbers = np.delete(numbers, np.where(numbers == perfect_squares_gt_500[0]))

# Find the perfect squares greater than 500 among the remaining cards without loops
mask_gt_500_second_player = numbers > 500
is_perfect_square_second_player = (np.sqrt(numbers) % 1 == 0)
perfect_squares_gt_500_second_player = numbers[mask_gt_500_second_player & is_perfect_square_second_player]

# Count the occurrences of perfect squares greater than 500 for the second player
count_prizes_second_player = np.sum(mask_gt_500_second_player & is_perfect_square_second_player)
total_simulations_second_player = len(numbers)

# Probability calculation for the second player
probability_second_player = count_prizes_second_player / total_simulations_second_player

print(f"Probability that the first player wins a prize: {probability_first_player:.4f}")
print(f"Probability that the second player wins a prize, given that the first player has won: {probability_second_player:.4f}")

print(f"Simulation results: {numbers[:100]}")

