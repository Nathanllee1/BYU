'''
This script picks a joke or a showerthought from reddit and prints it to the console.

Activate a virtual environment and install dependencies
$pipenv shell
or other virtualenv
$pip install -r requirements.txt
'''

import random
import praw
import urllib

#api info
reddit = praw.Reddit(client_id='NTli6KHgZM2Tkg', \
                     client_secret='MtCNRF0pRClhMaTFx73Ax6Vm4w8', \
                     user_agent='Shower Thoughts Bot') # don't mind this, just a project from earlier that I reused the credentials

#get user input
selection = input("Would you like a joke from r/jokes (A) or a showerthought from r/showerthought? (B)  ")

#select subreddit
selectedsub = reddit.subreddit(selection)
#sort by top
sortbytop = selectedsub.top

textbank = []

limit = 20

#for showerthouts (You only need the title)
def showerthoughts():
    for submission in sortbytop(limit):
        textbank.append(submission.title)
    picked = textbank[random.randint(0, limit)]
    return picked

#for jokes (You need the title and body)
def jokes():
    for submission in sortbytop(limit):
        textbank.append(submission.title + " " + submission.body)
        #textbank["title"].append(submission.title)
        #textbank["body"].append(submission.selftext)
    return textbank[random.randint(0, limit)]
print(showerthoughts)
#run scripts
if selection == 'A':
    print ("I'm picking a spicy piece of text from r/jokes")
    print (showerthoughts)
    print (textbank)
elif selection == "B":
    print ("I'm picking a spicy piece of text from r/showerthoughts")
    print(jokes)
else:
    print('Enter a letter try again')
#Most of it works, but it's not appendinig the list correctly resulting in it failing.  The structure works and the api requests are fine
#I'm not sure why it's not working, might need some help...I'm not sure if it's the python, because it seems right, but I don't know.
