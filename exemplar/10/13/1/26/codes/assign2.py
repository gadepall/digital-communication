import numpy as np
# Number of students in the class
total_students = 23
# Array representing the number of students from each house: A, B, C, D, E
students_per_house = np.array([4, 8, 5, 2, total_students - (4+8+5+2)])
# Calculate the total number of students from houses A, B, and C using NumPy
sim=np.random.choice(students_per_house,size=5,replace=False)
total_students_abc = np.sum(students_per_house[:3])
# Calculate the probability that the selected student is not from A, B, or C using NumPy
probability_not_abc = (total_students-total_students_abc) / total_students
print("Probability that the selected student is not from A, B, or C:",(total_students-total_students_abc),'/',total_students,'=',probability_not_abc)
print(f"simulation{sim}")