def fibonacci(n):
    if n <= 0:
        return
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

n = 10 
print(f"Fibonacci number at position {n} is {fibonacci(n)}")

def fibonacci_rec(n):
    if n <= 0:
        return
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)
    
n = 10
print(f"Fibonacci number at position {n} is {fibonacci_rec(n)}")
