# Euclidean algorithm
def gcd_euclidean(a, b):
    """
    Calculate the GCD of two numbers using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

# Naive algorithm
def gcd_naive(a, b):
    """
    Calculate the GCD of two numbers using a naive approach.
    """
    if a == 0:
        return b
    if b == 0:
        return a

    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd

# Example usage
if __name__ == "__main__":
    a = 48
    b = 18
    print(f"GCD of {a} and {b} using Euclidean algorithm: {gcd_euclidean(a, b)}")
    print(f"GCD of {a} and {b} using Stein's algorithm: {gcd_stein(a, b)}")
    print(f"GCD of {a} and {b} using naive algorithm: {gcd_naive(a, b)}")
