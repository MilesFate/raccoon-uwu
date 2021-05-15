import random
from random import randint
import time

lop=randint(1,4)
op=input('what is your question to the magic 8 ball? ')

if(lop==1):
    time.sleep(4)
    print('maybe')
if(lop==2):
    time.sleep(4)
    print('yes')
if(lop==3):
    time.sleep(4)
    print('no')
if(lop==4):
    time.sleep(4)
    print('depends')
