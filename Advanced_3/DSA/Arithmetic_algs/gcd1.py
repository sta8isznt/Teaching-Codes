def naive_gcd(a, b):
    if a == 0 or b == 0:
        return -1
    gcd = 1
    for i in range(1, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd

print(naive_gcd(20, 10))