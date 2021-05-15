import random
import time
from random import randint


from datetime import datetime
startTime = datetime.now()

chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+/`~ABCDEFGHIJKLMNOPQRSTUVWXYZ'

numbes = randint(1,10)
numbes = int(numbes)

length = randint(8,16)
length = int(length)

for p in range(numbes):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)


print(datetime.now() - startTime)