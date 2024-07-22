def recursive_fibonacci(number: int) -> int:
    if number < 2:
        return number
    return recursive_fibonacci(number - 1) + recursive_fibonacci(number - 2)
