# Given probabilities
probability_math_fail = 0.30  # Probability of failing in mathematics
probability_physics_fail = 0.25  # Probability of failing in physics
probability_both_fail = 0.10  # Probability of failing in both

# Probability of failing in physics given failing in mathematics (P(P | M))
probability_physics_given_math_fail = probability_both_fail / probability_math_fail

# Print the result
print("Probability of failing in physics given failing in mathematics:", probability_physics_given_math_fail)
