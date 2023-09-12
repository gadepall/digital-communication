import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
turns = int(100)
prob =0.5
pr_A = bernoulli.rvs(size=turns,p=prob)
pr_B = bernoulli.rvs(size=turns,p=prob)
for i in range(turns):
	if(pr_A[i] == 1):
		C = True
	else:
		C = False
	if(pr_B[i] == 1):
		D = True
	else:
		D = False
	And_op = C*D
	Or_op = C+ D
	if (And_op == Or_op):
		print(i)
		print("P(A)=P(B)=1 for P(A+B)=P(AB)")
		break
