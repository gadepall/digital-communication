import random
import scipy.stats as stats

# Set the number of questions and possible answers
num_questions = 5
num_answers = 3

# Set the number of simulations
num_simulations = 100000

# Set the probability of guessing the correct answer
guess_prob = 1 / num_answers

# Initialize the count of successful simulations
success_count = 0

# Perform the simulations
for _ in range(num_simulations):
    correct_count = 0  # Count of correct answers

    # Guess the answers for each question
    for _ in range(num_questions):
        if random.random() < guess_prob:
            correct_count += 1

    # Check if the candidate got four or more correct answers
    if correct_count >= 4:
        success_count += 1

# Calculate the simulated probability
simulated_probability = success_count / num_simulations

# Calculate the theoretical probability using the binomial distribution
theoretical_probability = 1 - stats.binom.cdf(3, num_questions, guess_prob)

# Print the results
print("Simulated Probability:", simulated_probability)
print("Theoretical Probability:", theoretical_probability)

