from scipy.stats import bernoulli
import numpy as np

# Total number of cards in the deck
total_cards = 52

# Probability of selecting the ace of spades
prob_ace_of_spades = 1 / total_cards

# Probability of selecting an ace
prob_ace = 4 / total_cards

# Probability of selecting a black card
prob_black_card = 26 / total_cards

# Simulate the card selection process using Bernoulli distribution
num_simulations = 100000  # Number of simulations
simulated_results = bernoulli.rvs(prob_ace_of_spades, size=num_simulations)

# Calculate simulated probabilities
simulated_prob_ace_of_spades = np.mean(simulated_results)
simulated_prob_ace = np.mean(bernoulli.rvs(prob_ace, size=num_simulations))
simulated_prob_black_card = np.mean(bernoulli.rvs(prob_black_card, size=num_simulations))


simlen=int(52)
prob = 1/52
data_bern = bernoulli.rvs(size=simlen,p=prob)
print(f"Probability of ace of spades: {prob_ace_of_spades:.4f}")
print(f"Simulated probability of ace of spades: {simulated_prob_ace_of_spades:.4f}")
print("Samples generated:",data_bern)




prob1 = 4/52
data_bern2 = bernoulli.rvs(size=simlen,p=prob1)
print(f"Probability of ace: {prob_ace:.4f}")
print(f"Simulated probability of ace: {simulated_prob_ace:.4f}")
print("Samples generated:",data_bern2)

prob2 = 26/52
data_bern3 = bernoulli.rvs(size=simlen,p=prob2)
print(f"Probability of black card: {prob_black_card:.4f}")
print(f"Simulated probability of black card: {simulated_prob_black_card:.4f}")
print("Samples generated:",data_bern3)





