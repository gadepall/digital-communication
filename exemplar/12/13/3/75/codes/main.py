import numpy as np

# Define the number of simulations
num_simulations = 100000

# Initialize a counter for successful outcomes
successful_outcomes = 0

for _ in range(num_simulations):
    # Initialize the bag with 5 red and 3 blue balls
    bag = np.array(['red', 'red', 'red', 'red', 'red', 'blue', 'blue', 'blue'])

    # Draw 3 balls without replacement
    drawn_balls = np.random.choice(bag, size=3, replace=False)

    # Check if exactly 2 of the 3 balls are red and the first ball is red
    if np.sum(drawn_balls == 'red') == 2 and drawn_balls[0] == 'red':
        successful_outcomes += 1

# Calculate the probability
probability = successful_outcomes / num_simulations

print(f"The probability that exactly two of the three balls were red, with the first ball being red, is approximately: {probability:.4f}")

