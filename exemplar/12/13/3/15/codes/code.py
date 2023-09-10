import numpy as np
X_values = np.array([0, 500, 2000, 3000])
X_probabilities = np.array([9995/10000, 3/10000, 1/10000, 1/10000])
num_simulations = 100000  
results = np.random.choice(X_values, num_simulations, p=X_probabilities)
average_winnings = np.mean(results)

print(f"Average winnings per ticket over {num_simulations} simulations: Rs. {average_winnings:.2f}")

