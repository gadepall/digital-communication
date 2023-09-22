from sympy import symbols, expand

# Define the symbolic variable z
z = symbols('z')

# Define the probabilities of hitting the target for A, B, and C
probabilities = [0.4, 0.3, 0.2]

# Calculate the Z-transforms for X, Y, and Z
M_X = (1 - probabilities[0]) + probabilities[0] * z
M_Y = (1 - probabilities[1]) + probabilities[1] * z
M_Z = (1 - probabilities[2]) + probabilities[2] * z

# Calculate the Z-transform for S (S = X + Y + Z)
M_S = M_X * M_Y * M_Z

# Expand the expression and find the coefficient of the z^2 term
M_S_expanded = expand(M_S)
coeff_z_squared = M_S_expanded.coeff(z, 2)

# The probability of two hits is the coefficient of z^2
probability_two_hits = coeff_z_squared

print("The probability of two hits:", probability_two_hits)

