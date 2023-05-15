import numpy as np
import matplotlib.pyplot as plt
import math as mt
def F_y(y):
    if y < 1:
        return 0
    elif y>=1 and y<=6:
        return mt.floor(y)/6
    else:
        return 1;
def func(k):
    sum=0
    for j in range(mt.floor(k/6)+1,7):
        sum=sum+F_y(k/j)
    return sum
def F_z(n):       
    return((mt.floor(n/6)+func(n))/6)
#the pmf list is made
#make it numpy array and proceed


print("Assignment 1: Question exemplar 10.13.3.21")

print("Probability that product of the die is 6",F_z(6)-F_z(5))

print("Probability that product of the die is 12",F_z(12)-F_z(11))

print("Probability that product of the die is 7",F_z(7)-F_z(6))




