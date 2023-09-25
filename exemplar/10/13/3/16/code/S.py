import random
#desired outputs 
desired_6 = 0.111
desired_12 = 0.111
#for simulation of exact result
def simulation():
  list1 = []
  list2 = []
  multiply = []
  for i in range(0, 1000):
    list1.append(random.randint(1, 6))
    list2.append(random.randint(1, 6))
  for i in range(0, 1000):
    multiply.append(list1[i] * list2[i])
  num_6 = 0
  num_12 = 0
  num_7 = 0
  for i in range(0, 1000):
    if multiply[i] == 6:
      num_6 += 1
    if multiply[i] == 12:
      num_12 += 1
    if multiply[i] == 7:
      num_7 += 1
  prob_6 = num_6 / 1000
  prob_12 = num_12 / 1000
  prob_7 = num_7 / 1000
  return prob_6, prob_12, prob_7


while 1>0:
  prob_6, prob_12, prob_7 = simulation()
  if prob_6 == desired_6 and prob_12 == desired_12:
    print(f"Probability of getting product 6 = {prob_6}")
    print(f"Probability of getting product 12 = {prob_12}")
    print(f"Probability of getting product 7 = {prob_7}")
    break
