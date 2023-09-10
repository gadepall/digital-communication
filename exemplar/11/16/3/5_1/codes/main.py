import numpy as np
import random
num_simulations = 100000
poss = np.arange(1,7)
weight = np.where(poss % 2 == 0, 1, 2)
simulation = random.choices(poss ,  weights = weight,cum_weights = None, k=10000)
x,prob = np.unique(simulation, return_counts = True)
probability = prob/10000
print(probability)
print("P(G>3)=", probability[3]+probability[4]+probability[5])
