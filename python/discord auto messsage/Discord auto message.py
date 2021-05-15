from pip._vendor import requests
import time


#this is the message sent, can be text, gifs, and videos
payload = {
    'content' : " " 
}

#this lets the script use the account
header = {
    'authorization': '' # discord token goes here
}

# this allows for the message to be sent multiple times
i = 0
while True:
    r = requests.post(' ',data= payload,headers=header) # the blank spot is the channel you wish to send the message too
    time.sleep(4)
    if i == 420:
        break
    i += 1 

