import numpy as np
from scipy.stats import bernoulli
num_students = 100000
num_questions = 20
p = 0.5  # Probability of a correct answer

x = np.random.binomial(1, p, size=(num_students, num_questions))
y = bernoulli.rvs(size=num_questions, p=p)
marks_per_student = np.sum(x == y, axis=1)
passing_students = np.sum(marks_per_student >= 12)
probability = passing_students / num_students
print(probability)

