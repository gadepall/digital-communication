def checker(num):
    if (num % 2) == 0:
        return 1
    else:
        return 0

print("Assignment 1: Question 12.13.2.12\n")
print("The total number of possible cases is counted by the variable 'count'.")
print("The number of required outcomes is counted by the variable 'c'.")
print("The probability is calculated by the variable 'p'.\n")

def main():
    count = 0
    c = 0
    for i in range(1,7,1): # i, j, k are the outcomes of the three die
        for j in range(1,7,1):
            for k in range(1,7,1):
                if checker(i) and checker(j) and checker(k): #counting the cases where all three outcomes are even
                    c += 1
                count += 1 #total number of outcomes are counted
    p = 1 - (c/count) # probability of atleast one odd number is equal to (1 - probability of all being even)
    print("Total number of outcomes is {}.".format(count))
    print("Number of possible outcomes is {}.\n".format(c))
    print("The probability of atleast one odd number occuring is equal to (1 - Probability of all observations being even).\n")
    print("Probability of all three observations being even = c/count")
    print("Probability of atleast one observation being odd = 1 - (c/count)\n")
    
    print("Therefore, the required probability is {}.".format(p))
main()
