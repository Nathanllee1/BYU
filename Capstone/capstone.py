'''
This script picks a joke or a showerthought from reddit and prints it to the console.

Activate a virtual environment and install dependencies
$pipenv shell
or other virtualenv
$pip install -r requirements.txt
'''

import random
import praw

#api info
reddit = praw.Reddit(client_id='NTli6KHgZM2Tkg', \
                     client_secret='MtCNRF0pRClhMaTFx73Ax6Vm4w8', \
                     user_agent='Shower Thoughts Bot') # don't mind this, just a project from earlier that I reused the credentials

textbank = []

#number of results pulled
results = 20

def getSelection():
    #get user input
    selection = input("""Would you like a joke from r/jokes (A)
or a showerthought from r/showerthought? (B)
""")
    if selection == 'A':
        print ("I'm picking a spicy piece of text from r/showerthoughts")
        return 'jokes'

    elif selection == 'B':
        print ("I'm picking a spicy piece of text from r/showerthoughts")
        return 'showerthoughts'

def textpull(sub):
    for submission in reddit.subreddit(sub).top(limit=results):
        textbank.append(submission.title)
        picked = textbank[random.randint(0, results)]
        print(picked)


#run functions
while True:
    getSelection()
    subreddit = getSelection()
    textpull(subreddit)
