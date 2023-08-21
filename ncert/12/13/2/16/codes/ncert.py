# Given probabilities
# P(hindi) = p_H
# P(english) = p_E

p_H = 0.60
p_E = 0.40
p_both = 0.20

# (a) Probability that she reads neither Hindi nor English newspapers
p_neither = 1 - (p_H + p_E - p_both)
print("(a) Probability that she reads neither Hindi nor English newspapers:", p_neither)

# (b) Probability that she reads English newspaper given that she reads Hindi newspaper=p_E_H
p_E_H = p_both / p_H
print("(b) Probability that she reads English newspaper given Hindi newspaper:", p_E_H)

# (c) Probability that she reads Hindi newspaper given that she reads English newspaper=p_H_E
p_H_E = p_both / p_E
print("(c) Probability that she reads Hindi newspaper given English newspaper:", p_H_E)

