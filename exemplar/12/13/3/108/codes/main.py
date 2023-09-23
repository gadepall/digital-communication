# Define pr(A|B), pr(A) and pr(B)
pr_A_given_B = 0.25
pr_A = 0.25
pr_B = 0.1

# Calculate pr(AB) using the formula pr(AB) = pr(A|B) * pr(B)
pr_AB = pr_A_given_B * pr_B

# Check if pr(AB) is equal to pr(A) * pr(B)
if pr_AB == pr_A * pr_B:
    print("Since pr(AB) = pr(A|B) * pr(B) is true, we can conclude that A is independent of B.")
else:
    print("A is not necessarily independent of B for pr(A|B) = pr(A).")

# Optionally, you can print the values of pr(AB) and pr(A) * pr(B)
print(f"pr(AB): {pr_AB}")
print(f"pr(A) * pr(B): {pr_A * pr_B}")

