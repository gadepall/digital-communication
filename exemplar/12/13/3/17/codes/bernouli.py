from scipy.stats import bernoulli

# Probability of success (p) - selecting an envelope with no cash prize
total_envelope = 1000
no_of_100 = 10
no_of_50 = 100
no_of_10 = 200

p100 = no_of_100 / total_envelope
p50 = no_of_50 / total_envelope
p10 = no_of_10 / total_envelope

# Calculate the combined probability of selecting an envelope with no cash prize (X = 0)
probability_X_equals_0 = 1-(bernoulli(p100).pmf(1) + bernoulli(p50).pmf(1) + bernoulli(p10).pmf(1))

print("Probability of selecting an envelope with no cash prize (X = 0):", probability_X_equals_0)

