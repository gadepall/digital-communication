import math

# Defining the equation
def equation(p):
    return p * math.comb(5, 2) * p**2 * (1 - p)**3 - 9 * p * math.comb(5, 3) * p**3 * (1 - p)**2

# Calculate p directly
a = math.comb(5, 2)
b = math.comb(5, 3)

p = (1 * b) / (a + 9 * b)

print(f"The value of p is: {p}")

