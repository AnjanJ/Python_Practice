__author__ = 'anjan'


#Write a Python function, clip(lo, x, hi) that returns lo if x is less than lo; hi if x is greater than hi;
#and x otherwise. For this problem, you can assume that lo < hi.

#Don't use any conditional statements for this problem. ' \
#Instead, use the built in Python functions min and max.

def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    # Your code here
    return min(max(x, lo), hi)


print clip(-3.25, 6.5, 3.74)
print clip(-6.84, 1.37, 8.38)