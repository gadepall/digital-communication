# Given probabilities
P_A = 0.4
P_B = 0.8
P_B_given_A = 0.6

P_A_intersection_B = P_B_given_A * P_A

# Calculate P(A ∪ B)
P_A_union_B = P_A + P_B - P_A_intersection_B

print("P(A ∪ B) =", P_A_union_B)

