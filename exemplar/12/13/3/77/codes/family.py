import random

# Function to simulate a family with three children
def simulate_family():
    children = [random.choice(["boy", "girl"]) for _ in range(3)]
    return children

# Function to check if a family has at least one girl
def has_at_least_one_girl(family):
    return "girl" in family

# Number of simulations
num_simulations = 100000
count1 = 0
count2 = 0

# Simulate families and calculate probabilities
for _ in range(num_simulations):
    family = simulate_family()
    if family[0] == "girl":
        count1 = count1 + 1
    if has_at_least_one_girl(family):
        count2 = count2 + 1

# Calculate the conditional probability
prob = count1/count2

print("simulated probability:",prob)
print("theroetical probability:",4/7)

