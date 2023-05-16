import numpy as np

def calculate_probability(num_trials):
    count = 0
    a = np.random.randint(2, size=num_trials)
    b = np.random.randint(2, size=num_trials)
    c = np.random.randint(2, size=num_trials)
    d = np.random.randint(2, size=num_trials)

    # Let a 2*2 matrix denoted by x
    x = np.array([
    [a,b],
    [c,d]
    ]).reshape(num_trials, 2, 2)
     
    #deterninant of x is det
    det = np.linalg.det(x)
    count = np.count_nonzero(det>0)

    probability = count/ num_trials
    return probability

# Set the number of trials for the simulation
num_trials = 10000000

# Calculate the probability
probability = calculate_probability(num_trials)

print(f"The probability that the value of the determinant is positive is: {probability}")
