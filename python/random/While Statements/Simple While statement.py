import time as t
import random as r
from random import randint

# this is used for time i think
from datetime import datetime

# this starts a timer for the script
startTime = datetime.now()

u = randint(1,99999)
while u > -1:
    print(u)
    if(u == -1):
        break
    u -=1

p=0
while True:
    print('I Love You ' + str(p))
    if(p == 999):
        break
    p +=1
    
# this shows the time it took for the script to run
print(datetime.now() - startTime)