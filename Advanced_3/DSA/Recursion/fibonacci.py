import time

# Iterative Fibonacci (O(n))
def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

# Naive Recursive Fibonacci (O(2^n))
def fibonacci_rec(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)

# Function to compare execution times
def compare_fibonacci(n):
    print(f"Comparing execution time for n = {n}")

    # Measure iterative approach time
    start = time.time()
    result_iter = fibonacci(n)
    end = time.time()
    time_iter = end - start
    print(f"Iterative: Fibonacci({n}) = {result_iter}, Time Taken = {time_iter:.6f} seconds")

    # Measure recursive approach time
    start = time.time()
    result_rec = fibonacci_rec(n)
    end = time.time()
    time_rec = end - start
    print(f"Recursive: Fibonacci({n}) = {result_rec}, Time Taken = {time_rec:.6f} seconds")

# Test for different values of n
compare_fibonacci(10)
compare_fibonacci(30)
