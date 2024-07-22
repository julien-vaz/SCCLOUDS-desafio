from math import sqrt, floor


# The Sieve of Eratosthenes
def linear_prime(maximum: int) -> list:
    last_prime = floor(sqrt(maximum))
    numbers = [number for number in range(2, maximum)]
    prime_index = 0
    while True:
        current_prime = numbers[prime_index]
        for number in numbers:
            if number == current_prime:
                continue
            if number % current_prime == 0:
                numbers.remove(number)
        prime_index += 1
        if current_prime >= last_prime:
            break
    return numbers
