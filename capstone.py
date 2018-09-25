
import random
import praw
import urllib
#api info
reddit = praw.Reddit(client_id='NTli6KHgZM2Tkg', \
                     client_secret='MtCNRF0pRClhMaTFx73Ax6Vm4w8', \
                     user_agent='Shower Thoughts Bot')
print(reddit.read_only)
'''
#subreddit picker
memepages = ['DeepFriedMemes', 'MostBeautiful', 'WholesomeComics']
selectedsubreddit = memepages[random.randint(0, len(memepages))]

print ("I picked a spicy meme from "  + selectedsubreddit)

#select subreddit
selectedsub = reddit.subreddit(selectedsubreddit)
#sort by top
sortedsub = selectedsub.top

'''
#pull and download images
imagenum = 20

counter = 0
for entries in reddit.subreddit('DeeepFriedMemes'):
    image_url = entries.url
    print (entries.url)
    counter += 1

    urllib.urlretrieve(image_url, counter + ".jpg")


    if counter == imagenum:
        break
