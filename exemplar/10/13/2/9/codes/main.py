import numpy as np

def simulate_dice_rolls(num_rolls):
    X = np.random.randint(1,7,num_rolls)
    # Calculate the probability estimate
    probability_estimate = sum(X==1) / num_rolls
    
    return probability_estimate

# Simulate rolling a die 100,000 times
num_rolls = 100_000
estimated_probability = simulate_dice_rolls(num_rolls)

# Print the estimated probability
if estimated_probability == 0.5:
    print("Therefore, the given statement is correct")
else:
    print(f"Estimated Probability of Rolling a '1' after {num_rolls} rolls: {estimated_probability:.4f}")
# Expected output (should be close to 1/6 = 0.1667)
