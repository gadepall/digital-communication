import numpy as np

#Simulating alphabets from a to z in a random order
alphabets=np.array(list(map(chr,range(ord('a'),ord('z')+1))))
sim=np.random.choice(alphabets,size=26,replace=False)
sim_len=26

#probability of occurence of vowel
vowel=np.array(np.isin(alphabets,['a','e','i','o','u']))
pr_vowel=(np.sum(vowel))/sim_len

#probability of occurence of consonant
pr_con=(sim_len-np.sum(vowel))/sim_len

print(f"the probability of occurence of consonant is {pr_con}")
print(f"the probability of occurence of vowel is {pr_vowel}")
print(f"simulation:{sim}")
