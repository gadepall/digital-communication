# Define the probabilities
p_X1_0 = p_X1_1 = 0.5
p_X2_0_given_X1_0 = 0.25
p_X2_0_given_X1_1 = 0  # Probability of this case is 0
p_X2_1_given_X1_0 = 0  # Probability of this case is 0
p_X2_1_given_X1_1 = 1/7

# Calculate the conditional probability
p_TA_given_visible = (p_X1_0 * p_X2_0_given_X1_0) / (
    p_X1_0 * (p_X2_0_given_X1_0 + p_X2_1_given_X1_0) + p_X1_1 * (p_X2_0_given_X1_1 + p_X2_1_given_X1_1))
    
print(f"The probability that the letter came from TATANAGAR is: {p_TA_given_visible}")

