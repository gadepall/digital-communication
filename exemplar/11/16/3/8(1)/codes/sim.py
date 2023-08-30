import numpy as np

#numbers represent the events
values = [1, 2, 3, 4, 5]

#probabilities of events
desired_probabilities = [0.15, 0.20, 0.31, 0.26, 0.08]

sim_len=100000
# Generate simulated numbers with desired probabilities
simulated_numbers = np.random.choice(values, size=sim_len, p=desired_probabilities)

# Count the occurrences of each simulated number using NumPy functions
unique_numbers, counts = np.unique(simulated_numbers, return_counts=True)
counts_dict = dict(zip(unique_numbers, counts))

count_1 = counts_dict.get(1, 0)
count_2 = counts_dict.get(2, 0)
count_3 = counts_dict.get(3, 0)
count_4 = counts_dict.get(4, 0)
count_5 = counts_dict.get(5, 0)

#P(E1+E2)
case_1=(count_1+count_2)/sim_len
print(f"Probability of case 1 {case_1}")

#P(E1'E5')
case_2=(sim_len-count_1-count_5)/sim_len
print(f"Probability of case 2 {case_2}")

#P(E2+E3)
case_3=(count_2+count_3)/sim_len
print(f"Probability of case 3 {case_3}")

#P(E3+E4)
case_4=(count_3+count_4)/sim_len
print(f"Probability of case 4 {case_4}")
