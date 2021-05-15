import itertools
import random
import string
from random import randint
from datetime import datetime

startTime = datetime.now()

#chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+/`~ABCDEFGHIJKLMNOPQRSTUVWXYZ'

chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation

#chars =  string.hexdigits + string.punctuation

numbes = 1
numbes = int(numbes)

length = 4
length = int(length)

for p in range(numbes):
    password = ''
    for c in range(length):
        password += random.choice(chars)

    def guess_password(real):
        chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation
        for password_length in range(3, 5):
            for guess in itertools.product(chars, repeat=password_length):
                guess = ''.join(guess)
                if guess == real:
                    return 'password is {}. '.format(guess)
    print(guess_password(password))
print('whoow he got a yankee with no brim')
print(datetime.now() - startTime)