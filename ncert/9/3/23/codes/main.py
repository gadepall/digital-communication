import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

n = 5 
#no of items
p = 0.5  
#probability of defective items
k = np.arange(0, n+1)  
binomial_pmf = binom.pmf(k, n, p)
mu = n * p
sigma = np.sqrt(n * p * (1 - p))
x = np.linspace(0, n, 100000)
normal_pdf = norm.pdf(x, mu, sigma)
normal_ans1=norm.pdf((1-mu)/sigma,mu,sigma)
print("answer through normal dist: ",normal_ans1)
binomial_ans2=binom.pmf(1,n,p)
print("answer through binomial dist: ",binomial_ans2)
binom_ans2 = binom.pmf(1, n, p)
plt.stem(k, binomial_pmf, label='PMF', basefmt='b-')
plt.plot(x, normal_pdf, label='PDF', color='r')
plt.axvline(x=1, color='g', linestyle='--', label='x=3')
plt.xlabel('Number of Defective Articles')
plt.ylabel('Probability')
plt.legend()
plt.savefig("./figs/fig1.png")
