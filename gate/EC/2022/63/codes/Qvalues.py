import scipy.stats as stats

# Define the value of x for which you want to calculate Q(x)
x = 1  # Replace with your desired value

# Calculate the Q function for x using the cumulative distribution function (CDF)
q_value = 1 - stats.norm.cdf(x)

# Print the result
print(f'Q({x}) = {q_value}')
print(f'Q({x}) = {1-q_value}')
