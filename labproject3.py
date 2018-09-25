import random
import time
name = ''

def askName():
    print ('What is your name')
    name = input()
    print ('Hey ' + name)
    print ('You get 3 guesses')
    return name



def exposition():
    print (name + ' is in a land full of dragons. In front of '+ name )
    time.sleep(2)
    print(name + ' sees two caves. In one cave, the dragon is friendly ')
    time.sleep(2)
    print('and will share his treasure with ' + name + '. The other dragon')
    time.sleep(2)
    print(' will not and eat you')

def cavechoice():
    cave = input('Pick a cave 1 or 2 or 3:  ')
    friendlycave = random.randint(1,3)

    if cave == friendlycave:
        print('You found a nice cave with a nice dragon')
    else:
        print('You got eaten')

def playagain():
    userplayagain = input('do you want to play again?')
    if userplayagain == 'yes':
        exposition()

name = askName()
exposition()
cavechoice()
playagain()
