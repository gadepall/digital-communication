
from scipy.stats import bernoulli
import numpy as np
# Given probabilities
Pr_A = 2/5
Pr_B = 3/10
Pr_AB = 1/5

# Calculate Pr(A') and Pr(B')
Pr_A_complement = 1 - Pr_A
Pr_B_complement = 1 - Pr_B

# Calculate Pr(A' ∩ B')
Pr_A_complement_and_B_complement = 1 - Pr_A - Pr_B + Pr_AB

# Calculate Pr(B' | A')
Pr_B_complement_given_A_complement = Pr_A_complement_and_B_complement / Pr_A_complement

# Calculate Pr(A' | B')
Pr_A_complement_given_B_complement = Pr_A_complement_and_B_complement / Pr_B_complement

# Calculate Pr(A' | B') * Pr(B' | A')
result = Pr_A_complement_given_B_complement * Pr_B_complement_given_A_complement

print(f"Pr(A' | B') * Pr(B' | A') = : {result:.8f}")



simulated_results = bernoulli.rvs(result, size=1000000)
simulated_prob = np.mean(simulated_results)
data_bern = bernoulli.rvs(size=10,p=result)
print(f"Simulated probability : {simulated_prob:.8f}")
print("Samples generated:",data_bern)
