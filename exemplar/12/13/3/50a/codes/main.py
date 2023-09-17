import numpy as np
E_x= 2.94
known_values =[1,2,4]
prob =[1/2,1/5,3/25,1/10,1/25,1/25]
A = (E_x*50 - 69)/26
known_values.append(2*A)
known_values.append(3*A)
known_values.append(5*A)

# Generate simulation
sim_len=1000000
random_variable = np.random.choice(known_values,sim_len, p=prob)
#finding variance of x
var_x=np.var(random_variable)
print(var_x)
