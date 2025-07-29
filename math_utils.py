from statistics_utils import calculate_variance

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def analyze_data(data):
    variance = calculate_variance(data)
    return variance
