a, b = (input("Enter the probability of A in fraction ")).split("/")
c, d = (input("Enter the probability of B in fraction ")).split("/")
from fractions import Fraction
fr1 = Fraction(int(a),int(b))
fr2 = Fraction(int(c),int(d))
pr1 = ((1-fr1)*fr2) + ((1-fr2)*fr1)
pr = pr1 + (fr1*fr2)
print("Probability that problem is solved is " + str(pr))
print("Probability that exactly one solved the problem is " + str(pr1))
