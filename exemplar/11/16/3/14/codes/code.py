import numpy as np

# Define the word
word = "ASSASSINATION"

# Number of simulations
num_simulations = 100000

# Counters for each scenario
count_a = 0  # Four consecutive S's
count_b = 0  # Two I's and two N's together
count_c = 0  # All A's not together
count_d = 0  # No two A's together

for _ in range(num_simulations):
    # Shuffle the letters
    shuffled_word = ''.join(np.random.permutation(list(word)))
    
    # Scenario a) Four consecutive S's
    if 'SSSS' in shuffled_word:
        count_a += 1
    
    # Scenario b) Two I's and two N's together
    if ('II' in shuffled_word) and ('NN' in shuffled_word):
        count_b += 1
    
    # Scenario c) All A's not together
    if 'AAAA' not in shuffled_word:
        count_c += 1
    
    # Scenario d) No two A's together
    if 'AA' not in shuffled_word:
        count_d += 1

# Calculate probabilities
prob_a = count_a / num_simulations
prob_b = count_b / num_simulations
prob_c = count_c / num_simulations
prob_d = count_d / num_simulations

# Print probabilities
print(f"Probability of four consecutive S's: {prob_a:.4f}")
print(f"Probability of two I's and two N's together: {prob_b:.4f}")
print(f"Probability of all A's not together: {prob_c:.4f}")
print(f"Probability of no two A's together: {prob_d:.4f}")

