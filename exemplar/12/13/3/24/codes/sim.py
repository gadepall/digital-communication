import numpy as np

# Define the values and their probabilities
values = [0, 1, 2, 3, 4]
probabilities = [0.1, 0.25, 0.3, 0.2, 0.15]

# Generate simulation
sim_len=1000
random_variable = np.random.choice(values,sim_len, p=probabilities)
#finding variance of x
var_x=np.var(random_variable)
#variance of x/2
var_x_2=np.var(random_variable/2)

print(var_x,var_x_2)
