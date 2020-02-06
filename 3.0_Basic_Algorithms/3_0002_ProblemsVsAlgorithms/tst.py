def sqrt(number):
    """
    Takes in a number and returns its square root
    """
    if number < 0:
        return None
    if (number==0) or (number ==1):
        return number
    else:
        return number**(1/2)



print(sqrt(4))
print(sqrt(25))
print(sqrt(0))
print(sqrt(-1))
print(sqrt(625))
print(sqrt(27))
