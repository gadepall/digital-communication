from scipy.stats import bernoulli
import numpy as np

AB=bernoulli.rvs(size=10000,p=7/10)
B=bernoulli.rvs(size=10000,p=17/20)
c1=np.sum(AB)
c2=np.sum(B)
print("P(A|B)=",c1/c2)
