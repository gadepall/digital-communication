# Define the probability of a student not being a swimmer
p_not_swimmer = 1/5

# Define the probability of a student being a swimmer
p_swimmer = 1 - p_not_swimmer

# Define the probability of four out of five students being swimmers
p_four_swimmers = p_swimmer**4 * p_not_swimmer

# Print the probability of four out of five students being swimmers
print("The probability of four out of five students being swimmers is:", p_four_swimmers)

