a,b = (input("Enter Pr(E) in fraction ")).split("/")
c,d = (input("Enter Pr(F) in fraction ")).split("/")
e,f = (input("Enter Pr(EF) in fraction ")).split("/")
from fractions import Fraction
fr1 = Fraction(int(a),int(b))
fr2 = Fraction(int(c),int(d))
fr3 = Fraction(int(e),int(f))
if fr3==fr1*fr2:
    print("Events E and F are Independent")
else :
    print("Events E and F not independent")
