# Given probabilities
pr_B = 3/5
pr_A_given_B = 1/2
pr_A_plus_B = 4/5

# Calculate the probability of A and B being independent
pr_AB = pr_A_given_B * pr_B
pr_A = pr_A_plus_B - pr_B + pr_AB
pr_A_complement = 1 - pr_A

# Calculate the probability of P(A + B)' and P(A' + B)
pr_A_plus_B_complement = 1 - pr_A_plus_B
pr_A_complement_plus_B = pr_A_complement  + pr_AB

# Calculate the final probability
result = pr_A_plus_B_complement + pr_A_complement_plus_B

print("The required probability is:", result)

