from scipy.stats import bernoulli
import numpy as np

#A and B are mutually exclusive so, P(AB)=0 
#P(A+B)=P(A)+P(B)-P(AB)=P(A)+P(B)
#So,
Por = 0.35 + 0.45 - 0
A = bernoulli.rvs(size=10000, p=0.35)
B = bernoulli.rvs(size=10000, p=0.45)
ApB = bernoulli.rvs(size=10000, p=0.8)
AB = bernoulli.rvs(size=10000, p=0)

ca = np.sum(1 - A)
cb = np.sum(1 - B)
cabp = np.sum(ApB)
cabm = np.sum(AB)
cab1 = np.sum(A - AB)
cabp1 = np.sum(1 - ApB)

print("P(A')=",ca / 10000)
print("P(B')=",cb / 10000)
print("P(A+B)=",cabp / 10000)
print("P(AB)=",cabm / 10000)
print("P(AB')=",cab1 / 10000)
print("P(A'+B')=",cabp1 / 10000)
