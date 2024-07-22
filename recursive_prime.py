from math import sqrt, floor


# The Sieve of Eratosthenes
def recursive_prime(maximum: int) -> list:
    last_prime = floor(sqrt(maximum))
    numbers = [number for number in range(2, maximum)]
    prime_index = 0
    return prime(last_prime, numbers, prime_index)

def prime(last_prime: int, numbers: list, prime_index: int) -> list:
    current_prime = numbers[prime_index]
    for number in numbers:
        if number == current_prime:
            continue
        if number % current_prime == 0:
            numbers.remove(number)
    if current_prime >= last_prime:
        return numbers
    prime_index += 1
    return prime(last_prime, numbers, prime_index)
