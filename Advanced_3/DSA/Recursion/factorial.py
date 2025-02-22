# Factorial of a number
def factorial_iter(n):
    """Iteratively"""
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

def factorial_rec(x):
    """Recursively"""
    if x == 0:
        return 1
    res = x * factorial_rec(x-1)
    return res
    

n = 100
print(factorial_rec(n))
print(factorial_iter(n))
    