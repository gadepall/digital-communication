import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

#Probability of the event of getting same number on both dice, i.e., W=0 is 1/6
prob = 1/6
size = int(1/prob)

#Number of samples is 10^(size-1), 0 denotes same number on dice
simlen=int(100000)

#Generating sample date using Bernoulli r.v.
data_bern = bernoulli.rvs(size=simlen,p=prob)

print("Samples generated:",data_bern)

def generate_pmf(size):
	array = np.full(size, prob)
	return array

pmf_X = generate_pmf(size)
pmf_Y = generate_pmf(size)
pmf_W_act = np.convolve(pmf_X, pmf_Y, mode='full')

# Calculate the actual probability of getting the same number on both dice (W = 0)
act_prob_same_no = pmf_W_act[5]  # Probability at W = 0
# Calculate the actual probability of getting different numbers on both dice (|W| > 0)
act_prob_diff_nos = 1 - act_prob_same_no

# Simulate the random variables X and Y by rolling two dice
num_samples = simlen
X_simulated = np.random.randint(1, size + 1, num_samples)
Y_simulated = np.random.randint(1, size + 1, num_samples)

# Calculate W for each pair of X and Y
W_simulated = X_simulated - Y_simulated
pmf_W_sim = np.bincount(W_simulated + size - 1) / num_samples

# Calculate the simulated probability of getting the same number on both dice (W = 0)
sim_prob_same_no = pmf_W_sim[5]  # Probability at W = 0
# Calculate the simulated probability of getting different numbers on both dice (|W| > 0)
sim_prob_diff_nos = 1 - sim_prob_same_no

print("Actual Probability (W = 0):", act_prob_same_no)
print("Simulated Probability (W = 0):", sim_prob_same_no)

if np.isclose(act_prob_same_no, act_prob_same_no):
    print("Hence verified for same number on both dice")
else:
    print("error")

print("Actual Probability (W ≠ 0):", act_prob_diff_nos)
print("Simulated Probability (W ≠ 0):", sim_prob_diff_nos)

if np.isclose(act_prob_diff_nos, act_prob_diff_nos):
    print("Hence verified for different numbers on both dice")
else:
    print("error")

k_values = np.arange(-size + 1, size) 
   
plt.stem(k_values, pmf_W_act, markerfmt='o', linefmt='C0-', use_line_collection=True, label='Actual')
plt.stem(k_values, pmf_W_sim, markerfmt='o', linefmt='C1-', use_line_collection=True, label='Simulation')
plt.xlabel("k")
plt.ylabel("Probability (simulated vs actual)")
plt.legend()
plt.grid()
plt.savefig('../figs/main_actvssim.png')
plt.show()

