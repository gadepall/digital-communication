import random
import numpy as np

def simulate(n):
    # Positions of the two persons of interest
    positions = np.array([random.sample(range(7), 2) for i in range(n)])
    diff_in_pos = np.abs(positions[:,0]-positions[:,1])
    prob = np.count_nonzero(diff_in_pos == 1)/n
    return prob

print("The probability that two particular people are adjacent to each other is:",simulate(10000))

