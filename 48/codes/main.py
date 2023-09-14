P_A = 0.50
P_B = 0.30
P_C = 0.20
P_D_given_A = 0.02
P_D_given_B = 0.02
P_D_given_C = 0.03

# Calculate P(D) using the law of total probability
P_D = P_A * P_D_given_A + P_B * P_D_given_B + P_C * P_D_given_C

# Calculate P(A | D) using Bayes' Theorem
P_A_given_D = (P_A * P_D_given_A) / P_D

print( P_A_given_D)
