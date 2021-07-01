# USEFUL IF YOU WANNA GET SERVER CURRENCY ON DISCORD (DANK MEMER)

from pynput.keyboard import Key,Controller
import time
import random

kbd = Controller()
text='pls beg'

def pause(t):
    while(t>0):
        print(f'Time Left : {t}')
        t-=1
        time.sleep(1)

input('press ENTER to start')
pause(3)

while True:
    kbd.type(text)
    kbd.press(Key.enter)
    kbd.release(Key.enter)
    print('Command Sent')
    pause(random.randint(41,60)) # RANDOM DELAY
    

