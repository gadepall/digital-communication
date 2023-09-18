import numpy as np
from sympy import symbols, Eq, solve

#Define symbol k
k = symbols('k')

#Define values of X and their corresponding probabilities
X = np.array([0.5, 1, 1.5, 2])
P = np.array([k, k**2, 2*k**2, k])

#Adding all entries of the array P
Sum = np.sum(P)

#Setting up an equation and solve for k 
equation = Eq(1, Sum)
solutions = solve(equation, k)

solutions = np.array(solutions)

#print the positive value of k
positive_k = solutions[solutions>0]
print("k=",positive_k)

#Using the positive value of k to find mean
k = positive_k
P = np.array([k, k**2, 2*k**2, k])

# Calculate the mean using a vectorized approach
mean = X@P

# Print the mean
print("Mean of X:", mean)
