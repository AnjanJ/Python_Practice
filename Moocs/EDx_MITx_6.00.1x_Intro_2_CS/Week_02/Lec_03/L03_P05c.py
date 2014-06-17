__author__ = 'anjan'
# L3 Problem 5c
#(3 points possible)

#3. Write a for loop that sums the values 1 through end, inclusive. end is a variable that we define for you.
# So, for example, if we define end to be 6, your code should print out the result:

#21

#which is 1 + 2 + 3 + 4 + 5 + 6.

#For problems such as these, do not include raw_input statements or define the variable end.
# Our automating testing will provide a value of end for you - so write your code in the
# following box assuming end is already defined.

end = 6
total = 0
for count in range(end+1):
    total += count

print total