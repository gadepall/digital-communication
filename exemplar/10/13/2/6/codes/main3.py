import numpy as np

# Generate 1000 random numbers between 1 and 360
random_numbers = np.random.randint(1, 361, size=10000)

# Define the ranges for the groups
group_ranges = [(1, 90), (90, 180), (180, 361)]

# Convert group ranges to numpy arrays
group_ranges = np.array(group_ranges)

# Calculate which group each random number belongs to
group_indices = np.argmax(np.where((random_numbers >= group_ranges[:, 0][:, np.newaxis]) & (random_numbers < group_ranges[:, 1][:, np.newaxis]), 1, 0), axis=0)

# Count the occurrences of each group
group_counts = np.bincount(group_indices, minlength=len(group_ranges))

# Calculate probabilities
total_samples = len(random_numbers)
prob = group_counts / total_samples

print("p_X(1) = ",prob[0])
print("p_X(2) = ",prob[1])
print("p_X(3) = ",prob[2])
