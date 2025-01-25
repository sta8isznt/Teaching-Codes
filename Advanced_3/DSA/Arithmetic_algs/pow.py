def pow(x, n):
    if n==1:
        return x
    res = pow(x, n//2)
    res *= res
    if n%2 ==1:
        res *= x
    return res

def pow_basic(x, n):
    res = 1
    for i in range(n):
        res *= x
    return res


# print(pow(5, 1000))
print(pow_basic(5, 1000))