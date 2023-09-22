# Define the probabilities of events A and B
P_A = 0.3   # Probability of event A happening
P_B = 0.6   # Probability of event B happening

# Calculate the probability of the intersection of A and B
P_A_and_B = P_A* P_B

# Calculate the complement probabilities of events A and B
P_A_complement = 1 - P_A
P_B_complement = 1 - P_B

# Calculate the probability of the complements A' and B' happening
P_A_complement_and_B_complement = P_A_complement * P_B_complement

# Calculate the probability of the intersection of complements A' and B'
P_intersection_complements = 1 - (P_A + P_B) + P_A_and_B

# Check if P(A' ∩ B') is approximately equal to P(A') * P(B')
if (P_intersection_complements - (P_A_complement * P_B_complement)) :
    print("A' and B' are independent events.")
else:
    print("A' and B' are not independent events.")

