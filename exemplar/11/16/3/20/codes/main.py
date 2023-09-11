# Total number of cards in the deck
total_cards = 52

# Number of red cards and black cards
red_cards = 26
black_cards = 26

# Probability of choosing the first card to be red
prob_red_first = red_cards / total_cards

# Probability of choosing the first card to be black
prob_black_first = black_cards / total_cards

# Probability of choosing the second card to be red after the first card chosen is red
prob_red_second_same_color = (red_cards - 1) / (total_cards - 1)

# Probability of choosing the second card to be black after the first card chosen is black
prob_black_second_same_color = (black_cards - 1) / (total_cards - 1)

# Probability of choosing the second card to be red after the first card chosen is black
prob_red_second = (red_cards ) / (total_cards - 1)

# Probability of choosing the second card to be black after the first card chosen is red
prob_black_second = (black_cards ) / (total_cards - 1)

# Probability of choosing the second card to be of a different color
prob_different_colors = prob_red_first * prob_black_second + prob_black_first * prob_red_second

print("Probability that the missing cards are of different colors:", prob_different_colors)

