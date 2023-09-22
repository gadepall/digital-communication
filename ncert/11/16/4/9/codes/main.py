import itertools

# Define the set of digits
digits = [0, 1, 3, 5, 7]

# Generate all possible 4-digit numbers with repeated digits
possible_numbers_1 = list(itertools.product(digits, repeat=4))

# Generate all possible 4-digit numbers without repeated digits
possible_numbers_2 = list(itertools.permutations(digits, 4))

# Filter numbers greater than 5000 for repetition case
possible_numbers_1 = [number for number in possible_numbers_1 if int(''.join(map(str, number))) > 5000]

# Filter numbers greater than 5000 for no repetition case
possible_numbers_2 = [number for number in possible_numbers_2 if int(''.join(map(str, number))) > 5000]

# Calculate the total number of possibilities for repetition case
total_possibilities_1 = len(possible_numbers_1)

# Calculate the total number of possibilities for non repetition case
total_possibilities_2 = len(possible_numbers_2)

# Function to check if a number is divisible by 5
def is_divisible_by_5(number):
    return number % 5 == 0

# Count the number of numbers divisible by 5 for case 1
count_divisible_1 = sum(1 for number in possible_numbers_1 if is_divisible_by_5(int(''.join(map(str, number)))))

# Count the number of numbers divisible by 5 for case 2
count_divisible_2 = sum(1 for number in possible_numbers_2 if is_divisible_by_5(int(''.join(map(str, number)))))

# Calculate the probability
probability_repeated = count_divisible_1 / total_possibilities_1
probability_not_repeated = count_divisible_2 / total_possibilities_2

print("Probability with repeated digits and greater than 5000:", probability_repeated)
print("Probability without repeated digits and greater than 5000:", probability_not_repeated)

