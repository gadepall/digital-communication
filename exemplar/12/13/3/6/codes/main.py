import math

def binomial_distribution(p, n, z):
  probabilities = []
  for k in range(n + 1):
    probabilities.append(math.comb(n,k)*(math.pow(p, k) * math.pow(1 - p, n - k)) * math.pow(z, k))

  return probabilities

import random
from collections import Counter

def toss_coin():
    return random.choice(['H', 'T'])  



def simulate_experiment(num_tosses):
    outcomes = random.choices(['H', 'T'], k=num_tosses)
    num_heads = outcomes.count('H')
    return num_heads
num_experiments = 10000


results = [simulate_experiment(3) for _ in range(num_experiments)]

head_distribution = dict(Counter(results))
print("Simulated Probability of getting 0 heads:", head_distribution[0]/num_experiments)
print("Simulated Probability of getting 1 head:", head_distribution[1]/num_experiments)
print("Simulated Probability of getting 2 heads:", head_distribution[2]/num_experiments)
print("Simulated Probability of getting 3 heads:", head_distribution[3]/num_experiments)


p = 1/2
n = 3
z = 1

probabilities = binomial_distribution(p, n, z)

print("Probability of getting 3 heads:", probabilities[3])
print("Probability of getting 2 heads:", probabilities[2])
print("Probability of getting 1 head:", probabilities[1])
print("Probability of getting 0 heads:", probabilities[0])

