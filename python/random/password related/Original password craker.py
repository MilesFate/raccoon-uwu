
import itertools
import string

from datetime import datetime
startTime = datetime.now()

def guess_password(real):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for password_length in range(8, 16):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return 'password is {}. found in {} guesses.'.format(guess, attempts)
print(guess_password('password'))

print(datetime.now() - startTime)