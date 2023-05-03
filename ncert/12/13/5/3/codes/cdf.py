from scipy.stats import binom

n,p = 10, 0.05

print(f"The cdf of the binomial distribution is {binom.cdf(1,n,p)}")
