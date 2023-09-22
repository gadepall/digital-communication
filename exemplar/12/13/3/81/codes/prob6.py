import math

from scipy.stats import bernoulli
import numpy as np
def binomial_coefficient(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def probability_of_3_heads(n, p):
    k = 3  # Number of heads
    q = 1 - p  # Probability of getting a tail
    probability = binomial_coefficient(n, k) * (p ** k) * (q ** (n - k))
    return probability

n = 8  # Total number of coin tosses
p = 0.5  # Probability of getting a head in one coin toss

result = probability_of_3_heads(n, p)
print(f"The probability of getting exactly 3 heads in {n} coin tosses is {result:.8f}")


simulated_results = bernoulli.rvs(result, size=1000000)
simulated_prob = np.mean(simulated_results)
data_bern = bernoulli.rvs(size=10,p=result)
print(f"Simulated probability : {simulated_prob:.8f}")
print("Samples generated:",data_bern)
