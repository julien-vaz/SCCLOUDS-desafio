def linear_fibonacci(number: int) -> int:
    fib1 = 0
    fib2 = 1
    for _ in range(number):
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
    return fib1
