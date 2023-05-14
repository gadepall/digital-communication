from scipy.stats import binom

# Set the number of trials (i.e., the number of times the die is thrown)
n = 2

# Set the number we're interested in (i.e., the number 5)
k = 5

# Set the probability of getting the number of interest on a single throw of the die
p = 1/6  # Probability of getting any particular number on a single throw of the die

# Probability of not getting k on any of the n throws
p_not_k = binom.cdf(0, n, p)

# Probability of getting k on at least one of the n throws
p_at_least_k = 1 - binom.cdf(0, n, p)

# Print the results
print("Probability of not getting {} on any of the {} throws: {:.4f}".format(k, n, p_not_k))
print("Probability of getting {} on at least one of the {} throws: {:.4f}".format(k, n, p_at_least_k))

