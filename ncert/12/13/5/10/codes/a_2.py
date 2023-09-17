import numpy as np

def simulate_lottery(p, n_lotteries, X):
    # Simulate the lottery results for each of the num_simulations trials
    #  num_simulations = X 
    trials_matrix = np.random.random((X, n_lotteries)) < p
    
    # Count the number of times each simulation wins a prize
    wins_per_simulation = np.sum(trials_matrix, axis=1)
    
    # Calculate the probabilities based on simulation results
    prob_at_least_once = np.count_nonzero(wins_per_simulation > 0) / X
    prob_exactly_once = np.count_nonzero(wins_per_simulation == 1) / X
    prob_at_least_twice = np.count_nonzero(wins_per_simulation >= 2) / X
    
    return prob_at_least_once, prob_exactly_once, prob_at_least_twice

# Parameters
p_lottery = 1/100
n_lotteries = 50
X = 1000000  # Adjust the number of simulations as needed

# Simulate and calculate probabilities
prob_at_least_once, prob_exactly_once, prob_at_least_twice = simulate_lottery(p_lottery, n_lotteries, X)

print(f"Simulated Probability of winning at least once: {prob_at_least_once:.8f}")
print(f"Simulated Probability of winning exactly once: {prob_exactly_once:.8f}")
print(f"Simulated Probability of winning at least twice: {prob_at_least_twice:.8f}")

