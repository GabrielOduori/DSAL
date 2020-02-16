"""
The **factorial** function is a mathematical function that multiplies a given
number, $n$, and all of the whole numbers from $n$ down to 1.

"""


def factorial(n):
    """
    Calculate n!

    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """
    if n==0:
        return 1
    return n * factorial(n-1)

print(factorial(4))
print("Pass" if (1==factorial(0))else "Fail")
print ("Pass" if  (1 == factorial(1)) else "Fail")
print ("Pass" if  (120 == factorial(5)) else "Fail")
