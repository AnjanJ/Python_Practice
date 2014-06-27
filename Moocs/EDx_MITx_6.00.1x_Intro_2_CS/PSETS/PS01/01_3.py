__author__ = 'anjan'
#Assume s is a string of lower case characters.
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
#For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#Longest substring in alphabetical order is: abc

s = 'azcbobobegghakl'
curr_char = ''
max_str = ''
pre_char = ''
curr_str = ''

for i in s:
    if i >= pre_char:
        curr_str += i
        if (len(curr_str) > len(max_str)):
            max_str = curr_str
    else:
        curr_str = i
    pre_char = i

print 'Longest common subsequence is :' +max_str