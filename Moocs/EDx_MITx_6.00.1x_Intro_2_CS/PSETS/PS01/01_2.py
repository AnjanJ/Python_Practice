__author__ = 'anjan'

# Counting bobs - (15 points possible)
#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s.
#For example, if s = 'azcbobobegghakl', then your program should print
#Number of times bob occurs is: 2


s = 'azcbobobegghakl'
to_find = 'bob'
count = 0

for i in range(len(s)):
    if s[i:i+3] == to_find:
        count += 1

print count
