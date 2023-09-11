import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

#100 samples
simlen=int(1000000)

#Probability of the event
prob = 0.5

#Generating sample date using Bernoulli r.v.
data_bern = bernoulli.rvs(size=simlen,p=prob)
#Calculating the number of favourable outcomes
err_ind = np.nonzero(data_bern == 1)
#calculating the probability
err_n = np.size(err_ind)/simlen

#Theory vs simulation
print(err_n,prob)
print(data_bern)

#Generating sample date using Bernoulli r.v.
data_bern2 = bernoulli.rvs(size=simlen,p=prob)
#Calculating the number of favourable outcomes
err_ind2 = np.nonzero(data_bern2 == 1)
#calculating the probability
err_n2 = np.size(err_ind2)/simlen

#Theory vs simulation
print(err_n2,prob)
print(data_bern2)


#Generating sample date using Bernoulli r.v.
data_bern3 = bernoulli.rvs(size=simlen,p=prob)
#Calculating the number of favourable outcomes
err_ind3 = np.nonzero(data_bern3 == 1)
#calculating the probability
err_n3 = np.size(err_ind3)/simlen

#Theory vs simulation
print(err_n3,prob)
print(data_bern3)

add = data_bern+data_bern2+data_bern3
count = add % 4 == 0
count2 = add % 2 == 0
fav=np.sum(count)
fav2=np.sum(count2)
print("prob of getting 3 heads ", fav/simlen)
print("prob of getting atleast 2 heads ", fav2/simlen)



