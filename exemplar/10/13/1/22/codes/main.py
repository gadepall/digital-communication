import random

#probability of getting a bad egg
prob_bad = 0.035

#total number of eggs in the lot
total = 400

num_simulations = 10000  #number of simulations
total_bad = 0

for _ in range(num_simulations):
    #simulate each egg 
    bad_eggs = sum(1 for _ in range(total) if random.random() < prob_bad)
    total_bad += bad_eggs

#the expected number of bad eggs
expected_bad = total_bad / num_simulations

print("Expected number of bad eggs:", int(expected_bad))

