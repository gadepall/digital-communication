# Total number of pieces
total_pieces = 8 + 10

# Number of triangles and squares
num_triangles = 8
num_squares = 10

# Number of blue triangles and squares
num_blue_triangles = 3
num_blue_squares = 6

# Probabilities using random variables
p_triangle = num_triangles / total_pieces
p_square = num_squares / total_pieces
p_blue_square = num_blue_squares / total_pieces
p_red_triangle = (num_triangles - num_blue_triangles) / total_pieces

print("Probability that the lost piece is a triangle:", p_triangle)
print("Probability that the lost piece is a square:", p_square)
print("Probability that the lost piece is a blue square:", p_blue_square)
print("Probability that the lost piece is a red triangle:", p_red_triangle)
