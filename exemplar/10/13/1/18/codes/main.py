import numpy as np
import matplotlib.pyplot as plt

# Define the range and number of random numbers to generate
lower_bound = 1
upper_bound = 52
num_numbers = 10000

# Generate random numbers
random_numbers = np.random.randint(lower_bound, upper_bound + 1, num_numbers)

# Count the numbers less than or equal to 6
count_less_than_six = np.count_nonzero(random_numbers <= 6)

# Print the result
#print("Number of random numbers less than or equal to 6:", count_less_than_six)
prob = count_less_than_six / num_numbers
print(prob)

def F_y(y):
    return np.where(y < 1, 0, np.where(y <= 13, np.floor(y) / 13, 1))

def func(n):
    j_range = np.arange(int(np.floor(n / 13)) + 1, 14)
    return np.sum(F_y(n / j_range))

n_values = np.arange(1, 53)
pmf_1 = (np.floor(n_values / 13) + np.vectorize(func)(n_values)) / 13 - (np.floor((n_values - 1) / 13) + np.vectorize(func)(n_values - 1)) / 13

# Plot the PMF
plt.stem(np.arange(1, 53), pmf_1)
plt.title('PMF: Probability of Selecting a Red Face Card (Z = k)')
plt.xlabel('k')
plt.ylabel('PMF')
plt.show()
