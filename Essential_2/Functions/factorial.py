# Factorial of a number
def factorial_iter(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

def factorial_rec(n):
    if n == 1:
        return 1
    else:
        return n * factorial_rec(n-1)
    
print(factorial_rec(4))
print(factorial_iter(4))
    
