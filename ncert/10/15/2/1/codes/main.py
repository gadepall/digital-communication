import numpy as np
import matplotlib.pyplot as plt

# Sample size for simulation
simlen = 10000
#Generating the samples for random variables x and y
x = np.random.choice(np.arange(0,5),size=simlen)
y = np.random.choice(np.arange(0,5),size=simlen)

#Calculating the pmf of Z
z, pmf_z = np.unique(x - y, return_counts = True)
z1, pmf_z1 = np.unique(abs(x-y), return_counts = True)

pmf_z = pmf_z/simlen
pmf_z1 = pmf_z1/simlen

#Cumulative probability of |Z| from simulation
cdf_z1 = np.cumsum(pmf_z1)


print("Probability through Simulation")
print("Same Day:", pmf_z1[0])
print("Consecutive Days:" , pmf_z1[1])
print("Different Days:", (1 - pmf_z1[0]))
print('')

#Calculating propability theoretically
print("Theoretical Probability")
theoretical = dict(map(lambda k: (k, (5-abs(k))/25), range(-4,5)))
print(theoretical)
#Cumulative probability
'''cdf_th = {0 : theoretical[0]}
cdf_th[1] = cdf_th[0] + theoretical[-1] + theoretical[1]
cdf_th[2] = cdf_th[1] + theoretical[-2] + theoretical[2]
cdf_th[3] = cdf_th[2] + theoretical[-3] + theoretical[3]
cdf_th[4] = cdf_th[3] + theoretical[-4] + theoretical[4]
'''
cdf_th = dict(map(lambda k : (k,sum(list(map(lambda i : (5-abs(i))/25, range(-k,k+1))))),range(0,5))) 
print(cdf_th)
#PMF of |Z|
pmf_z2 = list(map(lambda k : (5-abs(k))/25 + np.sign(k)*(5 - abs(k))/25 , range(0,5))) 

print("Same Day:" , pmf_z2[0])
print("Consecutive Days:" , pmf_z2[1])
print("Different Days:", 1- pmf_z2[0])


#Plotting graphs
plt.stem(z, theoretical.values(), linefmt='b-', markerfmt='bo')
plt.stem(z, pmf_z, linefmt='none', markerfmt='go')
plt.xlabel('$Z$')
plt.ylabel('PMF')
plt.title("PMF of Z")
plt.legend(['Theoretical', 'Simulated'])
plt.savefig('/home/devansh/EE23010/10.15.2.1/figs/figure1.png')
plt.clf()

plt.stem(z1, pmf_z2, linefmt='b-', markerfmt='bo')
plt.stem(z1, pmf_z1, linefmt='none', markerfmt='go')
plt.xlabel('$|Z|$')
plt.ylabel('PMF')
plt.title("PMF of |Z|")
plt.legend(['Theoretical', 'Simulated'])
plt.savefig('/home/devansh/EE23010/10.15.2.1/figs/figure2.png')
plt.clf()

plt.stem(z1, cdf_th.values(), linefmt='b-', markerfmt='bo')
plt.stem(z1, cdf_z1, linefmt='none', markerfmt='go')
plt.xlabel('$|Z|$')
plt.ylabel('CDF')
plt.title("CDF of |Z|")
plt.legend(['Theoretical', 'Simulated'])
plt.savefig('/home/devansh/EE23010/10.15.2.1/figs/figure3.png')
plt.clf()


