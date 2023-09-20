import numpy as np

def probability_less_than_9():
    favorable_outcomes = 0
    total_outcomes = 0

    for dice1 in range(1, 7):
        for dice2 in range(1, 7):
            total_outcomes += 1
            product = dice1 * dice2
            if product < 9:
                favorable_outcomes += 1

    probability = favorable_outcomes / total_outcomes
    return probability

probability = probability_less_than_9()

print(f"Probability that the product is less than 9: {probability:.4f}")

