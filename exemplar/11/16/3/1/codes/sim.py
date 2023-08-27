from itertools import permutations

word = "ALGORITHM"
all_permutations = set(map(lambda perm: ''.join(perm), permutations(word)))

random_variable = list(map(lambda perm: 1 if 'GOR' in perm else 0, all_permutations))

theoretical_prob=1/72
calculated_prob=sum(random_variable)/len(random_variable)
print(f"Theoretical probability = {theoretical_prob}")
print(f"calculated probabilty = {calculated_prob}")
