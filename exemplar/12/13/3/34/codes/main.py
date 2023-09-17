import random
import numpy as np

def theoretical_probability(n, p):
    if p < 1:
    	return "Not possible"
    elif p <= n:
        return (p - 1) / (n - 1)
    elif p > n:
        return 1

def simulate_probability(n, p, num_simulations=10000):
    selected_numbers = np.random.choice(np.arange(1, n + 1), size=(num_simulations, 2))
    s_values, r_values = selected_numbers[:, 0], selected_numbers[:, 1]

    # Exclude cases where s_values and r_values are equal
    non_equal_values = s_values != r_values
    s_values = s_values[non_equal_values]
    r_values = r_values[non_equal_values]

    favorable_outcomes = np.sum((r_values <= p) & (s_values <= p))
    favorable_outcomes2 = np.sum(s_values <= p)
    
    A = favorable_outcomes / num_simulations
    B = favorable_outcomes2 / num_simulations
    
    return (A / B)

n = 100  # Change n to any desired value
p = 50   # Change p to any desired value

theoretical_prob = theoretical_probability(n, p)
simulated_prob = simulate_probability(n, p, num_simulations=10000)

if theoretical_prob != "Not possible":
    print(f"Theoretical Probability: {theoretical_prob:.4f}")
else :
    print(f"Theoretical Probability: {theoretical_prob}")
print(f"Simulated Probability: {simulated_prob:.4f}")

