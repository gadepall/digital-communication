import math

# Define the number of each type of ball
num_orange = 3
num_green = 3
num_blue = 2

# Total number of balls in the box
total_balls = num_orange + num_green + num_blue

# Number of balls drawn
balls_drawn = 3

# Calculate the probability of drawing 2 green balls and 1 blue ball
probability = (math.comb(num_green, 2) * math.comb(num_blue, 1)) / math.comb(total_balls, balls_drawn)
print('Probability of getting 2 Green and 1 Blue is',probability)
