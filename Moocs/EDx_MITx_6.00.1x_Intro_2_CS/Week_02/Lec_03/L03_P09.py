__author__ = 'anjan'
#L3 Problem 9
#(5 points possible)

#In this problem, you'll create a program that guesses a secret number!

#The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
# The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search,
# the computer will guess the user's secret number!

low = 0
high = 100

msg = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."

value = low+high/2

print ('Please think of a number between 0 and 100!')
print ('Is your secret no: '+str(value)+'?')
option = raw_input(msg)

while option != 'c':
    if option == 'h':
        high = value
        value = (low + high) / 2


    elif option == 'l':
        low = value
        value = (low + high) / 2


    else:
        print ('Sorry, I did not understand your input.')
        print ('Is your secret no: '+str(value)+'?')
        option = raw_input(msg)

    print ('Is your secret no: '+str(value)+'?')
    option = raw_input(msg)

print('Game over. Your secret number was: '+str(value))