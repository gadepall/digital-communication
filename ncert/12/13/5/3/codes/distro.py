import math

def BinomialProbability(n,p,r) :
    pro = math.comb(n,r)*math.pow(1-p,n-r)*math.pow(p,r)
    return pro

def cdf(n,p,x) :
    if x == -1:
        return 0
    sum = BinomialProbability(n,p,x)
    return sum + cdf(n,p,x-1)

n = 10
p = 0.05

print(f"\nP(0) = Probability of X <= 1 is CDF(1) = {cdf(n,p,1)}")
