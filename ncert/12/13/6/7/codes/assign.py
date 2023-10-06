import numpy as np
from scipy.special import comb

# Probability of getting a six on a single roll
p_six = 1/6
# Probability of not getting a six on a single roll
p_not_six = 5/6

# Calculate the probability of getting the first two sixes in the first five throws
part1 = comb(5, 2) * (p_six**2) * (p_not_six**3)

# Calculate the probability of getting the third six on the sixth throw
part2 = p_six

# Calculate the overall probability
probability = part1 * part2

print(f"The probability of getting the third six on the sixth throw is approximately {probability:.3f}")

