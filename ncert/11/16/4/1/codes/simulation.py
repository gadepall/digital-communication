import math
import random

# Parameters of the problem
P = 3
Q = 4
R = 3
N = P+Q+R
p = 2
q = 2
r = 1
n = p+q+r

num_trials = 1000000
num_successes = 0   # Number of successful trials

for i in range(num_trials):
    # Draw n marbles from the box without replacement
    box = ['red']*P + ['blue']*Q + ['green']*R
    selected = random.sample(box, n)
    
    # Count the number of red, blue, and green marbles in the selection
    num_red = selected.count('red')
    num_blue = selected.count('blue')
    num_green = selected.count('green')
    
    if num_red == p and num_blue == q and num_green == r:
        num_successes += 1

probability = num_successes / num_trials
print('Simulated probability: ', probability)


def draw_probability(N, P, Q, R, n, p, q, r):
    N = P+Q+R
    n = p+q+r
    num_ways = math.comb(P, p) * math.comb(Q, q) * math.comb(R, r)
    total_ways = math.comb(N, n)
    probability = num_ways / total_ways
    return probability

print ("Formula Probability: ", draw_probability(N, P, Q, R, n, p, q, r))
