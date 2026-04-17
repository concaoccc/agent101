def factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def average(numbers: list) -> float:
    """Calculate the average of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot compute average of an empty list.")
    return sum(numbers) / len(numbers)