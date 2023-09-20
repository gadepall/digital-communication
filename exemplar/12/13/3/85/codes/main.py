import numpy as np
import scipy.stats as stats

#no. of questions
n=10

#probalility of correct
p=0.5

#no. of simulation
num=1000

# Simulate all exam attempts at once
guesses = np.random.choice([True, False], size=(num, n))
num_correct = np.sum(guesses, axis=1)
    
# Calculate the probability of at least 8 correct answers
at_least_eight = np.sum(num_correct >= 8)

#simulated
print("simulated probability: ",at_least_eight/num)
#theoretical
prob = 1 - stats.binom.cdf(7, n, p)
print("theroritical probability: ",prob)
