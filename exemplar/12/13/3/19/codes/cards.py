import random
import math
import numpy as np
import matplotlib.pyplot as plt

def simulate_four_kings():
    deck = [1] * 4 + [0] * 48  # 1 represents a king, 0 represents a non-king
    random.shuffle(deck)
    drawn_cards = deck[:4]
    if (sum(drawn_cards) == 4):
       return True

num_simulations = 1000000  # Number of simulations to run
count1 = 0 
 
for _ in range(num_simulations):
    if simulate_four_kings():
    	count1 = count1 + 1
           
prob1 = count1/num_simulations

print("Simulated Probability:")
print("probability 4 kings shown up =",prob1)

print("Theoretical Probability:")
print("probability 4 kings shown up =",math.comb(4,4)*math.comb(48,0)/math.comb(52,4))



