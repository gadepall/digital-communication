def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

total_numbers = 100
prime_count = sum(1 for num in range(1, total_numbers + 1) if is_prime(num))
probability = prime_count / total_numbers

print(f"The probability of prime numbers from 1 to {total_numbers} is: {probability:.2f}")

