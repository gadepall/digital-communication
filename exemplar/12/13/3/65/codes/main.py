# Define the probabilities
prob_A = 0.3  # Probability of event A
prob_B = 0.6  # Probability of event B

# Calculate the probabilities according to the statement
exactly_one_A_or_B = (1 - prob_A) * prob_B + prob_A * (1 - prob_B)

# Output the result
if exactly_one_A_or_B == prob_A * prob_B + (1 - prob_A) * prob_B + prob_A * (1 - prob_B):
    print("The statement is false.")
else:
    print("The statement is true.")

