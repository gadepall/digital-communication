import numpy as np

m = 100000
n = 500000
k = np.random.randint(1, 100001)


def simulation(m, n):
    # Create an array of length m+n with m ones and n zeroes
    ones = np.ones(m, dtype=int)
    zeroes = np.zeros(n, dtype=int)

    # Concatenate the ones and zeroes
    simulation = np.concatenate((ones, zeroes))

    # Shuffle the simulation
    np.random.shuffle(simulation)

    return simulation
sim=simulation(m,n);
if np.random.choice(sim) == 1:
    new_sim=simulation(m+k,n)
else:
    new_sim=simulation(m,n+k)
    
prob_white=np.sum(new_sim)/new_sim.shape[0]
print(f"k={k}")
print(f"probability of white ball : {prob_white}")
print(f"theoretical prob :{m/(m+n)}")																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																															
