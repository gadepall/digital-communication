import math
import matplotlib.pyplot as plt

def binomial_probability(n, k, p):
    coefficient = math.comb(n, k)
    probability = coefficient * (p ** k) * ((1 - p) ** (n - k))
    return probability

n = 4  # Number of coin tosses
p = 0.5  # Probability of getting a head

money_changes = [-6, -4.5, -3, -1.5, 1]
probabilities = []

for k in range(n + 1):
    probability = binomial_probability(n, k, p)
    probabilities.append(probability)

expected_value = sum(p * x for x, p in zip(money_changes, probabilities))

plt.scatter(money_changes, probabilities, marker='o')
plt.xlabel("Money Change (in Rs)")
plt.ylabel("Probability")
plt.title("Distribution of Money Changes")

# Join each point to the X-axis with solid lines
for x, p in zip(money_changes, probabilities):
    plt.plot([x, x], [0, p], color='gray', linestyle='-', lw=1)

# Save the image as a JPG file
plt.savefig("money_changes_distribution.jpg")

plt.show()


