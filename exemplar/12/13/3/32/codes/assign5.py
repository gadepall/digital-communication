# Probability of getting a head given that the coin is fair
#A = coin is fair, B = getting a heads
P_B_given_A = 0.5

# Prior probability that the coin is fair
P_A = 0.5

# Probability of getting a head, considering both possibilities
P_B = (P_B_given_A * P_A) + (1.0 * (1 - P_A))  # Using law of total probability

# Applying Bayes' Theorem
P_A_given_B = (P_B_given_A * P_A) / P_B

print(f"The probability that the coin is fair given that you got a head is: {P_A_given_B:.4f}")

