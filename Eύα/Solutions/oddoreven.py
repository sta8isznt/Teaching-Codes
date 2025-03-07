def oddoreven(num):
    """Returns wether the number is odd or even"""
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
number = int(input("Enter a number: "))
ans = oddoreven(number)
print(ans)
    
