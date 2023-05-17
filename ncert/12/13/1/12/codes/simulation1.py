import numpy as np

#Question : Assume that each born child is equally likely to be a boy or a girl. If a family has
#           two children, what is the conditional probability that both are girls given that
#           1) The youngest is a girl
#           2) At least one is a girl

#Solution : 

simlen=10000000

#let 1 represent 1st born child is boy and 2nd born child is a boy
#let 2 represent 1st born child is boy and 2nd born child is a girl
#let 3 represent 1st born child is girl and 2nd born child is a boy
#let 4 represent 1st born child is girl and 2nd born child is a girl

children = np.random.choice([1,2,3,4],size=simlen) #for 1st born child 
count_1 = (children ==1).sum()
count_2 = (children ==2).sum()
count_3 = (children ==3).sum()
count_4 = (children ==4).sum()

#part1
print("calculated = 0.5")
print("experimental =",(count_4/(count_3+count_4)))
#part2
print("calculated = 0.3333")
print("experimental =",(count_4/(count_3+count_4+count_2)))


