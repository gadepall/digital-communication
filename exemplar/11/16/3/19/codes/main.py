import numpy as np

def count_consecutive_numbers(simulation_length):
  random_numbers = np.random.randint(1, 21, (simulation_length, 3))
  random_numbers.sort()
#   print(random_numbers)
  consecutive_mask = np.all(np.diff(random_numbers, axis=1) == 1, axis=1)
#   print(consecutive_mask)
  count = np.sum(consecutive_mask)
  return count

simulation_length = 100000
count = count_consecutive_numbers(simulation_length)

print(f"Number of trials with consecutive numbers: {count}")

probability = count / simulation_length
required= 1-probability
print(f"Simulated Probability: {required:.4f}")

def calculate_combinations(n, k):
    # Calculate binomial coefficient C(n, k)
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    result = 1
    for i in range(1, min(k, n - k) + 1):
        result = result * (n - i + 1) // i
    return result

total_ways = calculate_combinations(20, 3) 

consecutive_ways = 18 

non_consecutive_ways = total_ways - consecutive_ways
theory=non_consecutive_ways/total_ways
print(f"Therotical probability: {theory:.4f}")


