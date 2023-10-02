from math import comb

# Given values
n = 5

# Calculate p_X(2)
p_2 = comb(n, 2) * (1/10)**2 * (9/10)**(n - 2)
p_2=round(p_2,4)

# Calculate p_X(3)
p_3 = comb(n, 3) * (1/10)**3 * (9/10)**(n - 3)

# Check if p_X(2) is equal to 9 times p_X(3)
if p_2 == 9 * p_3:
    # Calculate p
    p = 1 / 10
    print("The value of p is:",p)
else:
    print("No solution found.")

