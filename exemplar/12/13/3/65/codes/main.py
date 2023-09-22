# Given probabilities
pr_B = 3/5
pr_A_given_B = 1/2
pr_A_and_B = 4/5
pr_A = 1/2

# Calculate the probability of A' (not A)
pr_A_prime = 1 - pr_A

# Calculate the conditional probability of A' given B
pr_A_prime_given_B = 1 - pr_A_given_B

# Use Bayes' theorem to calculate P(B | A')
pr_B_given_A_prime = (pr_A_prime_given_B * pr_B) / pr_A_prime

print(f"The conditional probability P(B | A') is: {pr_B_given_A_prime}")

