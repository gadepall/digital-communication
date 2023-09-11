days = 365
b = int(days / 7)
# Calculate the remaining days after complete weeks
remaining_days = days % 7

# Probability of Tuesday
p_tue = (remaining_days / 7) * 1/7

# Probability of Wednesday
p_wed = (remaining_days / 7) * 1/7

# Overall Probability of Tuesday or Wednesday
p_tue_wed = p_tue + p_wed

# Check if it's the 53rd week
k = b + 1
if k == 53:
    print(f"The probability of having 53 Tuesday or 53 Wednesday is", p_tue_wed)
else:
    print("The total tuesdays and wednesdays in a year are not 53")
