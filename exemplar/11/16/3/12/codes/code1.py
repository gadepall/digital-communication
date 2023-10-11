#code by Muzaan Mohammed Faizel AP
#EE22BTECH11036
import numpy as np
# Define the probabilities
#QUESTION 1
p_A = 0.5
p_B = 0.7
p_AB = 0.6
p_sum = p_A + p_B - p_AB  # Compute the sum

# Create a NumPy array with the probabilities
arr1 = np.array([p_A, p_B, p_AB, p_sum])

# Check the consistency conditions
condition_1 = p_AB <= p_A*p_B  # Use '*' for element-wise multiplication
condition_2 = np.all((0 <= arr1) & (arr1 <= 1))  # Use 'np.all' to check all elements

# Check if conditions are met
print("Question 1:")
if condition_1 and condition_2:
    print("Probabilities are consistently defined.")
else:
    print("Probabilities are not consistently defined.")
    #QUESTION2
p_A = 0.5
p_B = 0.4
p_sum = 0.8
p_AB = p_A + p_B - p_sum  # Compute p(AB)

# Create a NumPy array with the probabilities
arr2 = np.array([p_A, p_B, p_AB, p_sum])

# Check the consistency conditions
condition_1 = p_AB <= p_A*p_B  # Use '*' for element-wise multiplication
condition_2 = np.all((0 <= arr2) & (arr2 <= 1))  # Use 'np.all' to check all elements

# Check if conditions are met
print("Question 2:")
if condition_1 and condition_2:
    print("Probabilities are consistently defined.")
else:
    print("Probabilities are not consistently defined.")    
