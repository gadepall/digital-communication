# Define the probabilities
pr_A = 1/6  # Probability of selecting Bag 1
pr_B = 2/6  # Probability of selecting Bag 2
pr_C = 3/6  # Probability of selecting Bag 3

pr_x_given_A= 0  # Probability of selecting a white ball from Bag 1 (0 white balls)
pr_x_given_B = 1/3  # Probability of selecting a white ball from Bag 2 (1 white ball)
pr_x_given_C = 1  # Probability of selecting a white ball from Bag 3 (3 white balls)

# Calculate conditional probabilities
pr_B_given_x1 = (pr_B * pr_x_given_B) / ((pr_A * pr_x_given_A) + (pr_B * pr_x_given_B) + (pr_C * pr_x_given_C))
pr_C_given_x1 = (pr_C * pr_x_given_C) / ((pr_A * pr_x_given_A) + (pr_B * pr_x_given_B) + (pr_C * pr_x_given_C))

# Print the conditional probabilities
print("Conditional Probability (Bag 2 | White Ball):", pr_B_given_x1)
print("Conditional Probability (Bag 3 | White Ball):", pr_C_given_x1)

