# Define the probability of not E or not F
prob_not_E_or_not_F = 0.25

# Calculate the probability of E and F using the complement rule
prob_E_and_F = 1 - prob_not_E_or_not_F

# Check if E and F are mutually exclusive
are_mutually_exclusive = prob_E_and_F == 0

# Output the result
if are_mutually_exclusive:
    print("Events E and F are mutually exclusive.")
else:
    print("Events E and F are not mutually exclusive.")
