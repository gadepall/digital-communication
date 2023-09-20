from scipy.stats import bernoulli
import numpy as np
import random

#taking independent parameters
A=bernoulli.rvs(size=10000,p=random.random())
B=bernoulli.rvs(size=10000,p=random.random())

#P(A'+B)
AUB=np.sum(np.logical_or(A==0, B==1))
#1-P(A)P(B')
form=np.sum(1-(A*(1-B)))
if AUB==form:
	print("P(A'+B)=1-P(A)P(B') proved")
