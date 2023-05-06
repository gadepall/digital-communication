a,b = (input("Enter the probability of A in fraction : ")).split("/")
c,d = (input("Enter the probability of B in fraction : ")).split("/")
e,f = (input("Enter the probability of notA or not B in fraction: ")).split("/")
from fractions import Fraction
fr1 = Fraction(int(a),int(b))
fr2 = Fraction(int(c),int(d))
fr3 = Fraction(int(e),int(f))
if fr1*fr2 == 1-fr3:
    print("A and B are independent")
else : 
    print(" A and B are not independent")


                                                                             

