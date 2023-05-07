A = float(input('Enter % of student studying mathematics : '))
assert A<=100 and A>=0 
Pr_A = A/100

B = float(input('Enter % of student studying biology : '))
assert B<=100 and B>=0
Pr_B = B/100

AB = float(input('Enter % of student studying both mathematics and biology : '))
assert AB>=(A + B)-100 and AB<=A + B
Pr_AB = AB/100

Pr_A_B = Pr_A + Pr_B - Pr_AB
assert Pr_A_B <=1 and Pr_A_B>=0
print('Pr(A + B) =',Pr_A_B)





