import random

# Function to simulate rolling a fair 6-sided die
def roll_die():
    return random.randint(1, 6)

# Function to simulate choosing a bag based on the die roll
def choose_bag():
    die_roll = roll_die()
    if die_roll in [1, 3]:
        return "Bag 1"
    else:
        return "Bag 2"

# Function to simulate drawing a ball from a chosen bag
def draw_ball(bag):
    if bag == "Bag 1":
        balls = ["Black", "Black", "Black", "White", "White", "White", "White"]
    else:
        balls = ["Black", "Black", "Black", "Black", "White", "White", "White"]
    return random.choice(balls)

# Number of simulations
num_simulations = 100000
black_count = 0

# Simulate the scenario and calculate the probability
for _ in range(num_simulations):
    chosen_bag = choose_bag()
    drawn_ball = draw_ball(chosen_bag)
    if drawn_ball == "Black":
        black_count += 1

# Calculate the probability of choosing a black ball
probability_black = black_count / num_simulations
print("Simulated Probability of Choosing a Black Ball:", probability_black)
print("actual probability of choosing a black ball:", 11/21)
