import itertools
import numpy as np

def calculate_probability():
    numbers = [0, 2, 3, 5]
    permutations = np.array(list(itertools.permutations(numbers, 4)))

    valid_permutations = permutations[permutations[:, 0] != 0]

    four_digit_numbers = (
        valid_permutations[:, 0] * 1000
        + valid_permutations[:, 1] * 100
        + valid_permutations[:, 2] * 10
        + valid_permutations[:, 3]
    )

    valid_count = np.sum(four_digit_numbers % 5 == 0)
    total_count = len(four_digit_numbers)

    probability = valid_count / total_count

    return probability

probability = calculate_probability()
print(f"The probability of forming a four-digit number with the numbers 0, 2, 3, and 5, without repetition, and the number being divisible by 5 is: {probability}")

