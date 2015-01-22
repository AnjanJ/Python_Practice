__author__ = 'anjan'
# The function rescuePower(base,exp)
# from Problem to computed base ** exp
# by decomposing the problem into one recursive case and one base case:
#
# base ** exp = base * base ** exp - 1 if exp > 0
# base ** exp = 1 if exp = 0
# Another way to solve this problem just using multiplication (and remainder) is to note that
# base ** exp = (base ** 2) ** exp/2  if exp > 0 and exp is even
# base ** exp = (base ** 2) ** exp-1  if exp > 0 and exp is odd
# base ** exp = 1                     if exp == 0
# Write a procedure recurPowerNew which recursively computes exponentials using this idea.

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if exp <= 0:
        return 1

    # Recursive case 1: exp > 0 and even
    elif exp % 2 == 0:
        return recurPowerNew(base*base, exp/2)

    # Otherwise, exp must be > 0 and odd, so use the second
    #  recursive case.
    return base * recurPowerNew(base, exp - 1)
print recurPowerNew(-6.33, 8)