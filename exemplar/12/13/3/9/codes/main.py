# Given probabilities
p1 = float(input("enter p1: "))  # Probability of E1
p2 = float(input("enter p2 : "))  # Probability of E2

# Calculate probabilities as described
prob_i = p1 * p2  # (i) p1 * p2
prob_ii = (1 - p1) * p2  # (ii) (1 - p1) * p2
prob_iii = 1 - (1 - p1) * (1 - p2)  # (iii) 1 - (1 - p1) * (1 - p2)
prob_iv = p1 + p2 - 2 * p1 * p2  # (iv) p1 + p2 - 2 * p1 * p2

# Print the results
print(f"(i)   {prob_i:.4f} - Both E1 and E2 occur simultaneously.")
print(f"(ii)  {prob_ii:.4f} - E1 does not occur, but E2 occurs.")
print(f"(iii) {prob_iii:.4f} - Either E1 or E2 or both E1 and E2 occur.")
print(f"(iv)  {prob_iv:.4f} - Either E1 or E2 occurs but not both.")
