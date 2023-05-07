a = float(input('Enter probability of A :'))
b = float(input('Enter probability of B :'))

P_NotA = (1-a)
P_NotB = (1-b)
P_AorB = (a + b - (a*b))

print('P(Not A) = ',P_NotA)
print('P(Not B) = ',P_NotB)
print('P(A or B) = ',P_AorB)