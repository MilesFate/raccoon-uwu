import random
import time
from random import randint
import string

from datetime import datetime
startTime = datetime.now()

#chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+/`~ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# this is what is above but better
#chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation
# this is what is above but better
chars =  string.hexdigits + string.punctuation

numbes = 1000000
numbes = int(numbes)

length = 8
length = int(length)


for p in range(numbes):
    password = ''
    for c in range(length):
        password += random.choice(chars)



print(datetime.now() - startTime)