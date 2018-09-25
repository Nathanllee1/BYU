import random

print('guess a numbers between 2 numbers')
start = int(input('Starting number:  '))
end = int(input('Ending number:  '))
guesses = int(input('How many guesses do you want?:  '))

guessesTaken = 0

print('Hello what is your name?')
name = input()
number = int(random.randint(start, end))
while guessesTaken < guesses:

    userguess = int(input('Guess your number:  '))

    guessesTaken += 1

    if userguess == number:
        guessesTaken = str(guessesTaken)
        print('You got it '+ name + 'in' + guessesTaken)
        break

    if userguess <= number:
        print ('Too low')

    if userguess >= number:
        print ('Too high')
number = str(number)
print ('Sorry you lost ' + name + 'The correct number was ' + number)
