# My library

import time

def currentTime():
    return time.ctime()

if __name__=='__main__':
    try:
        print("This will print the current time every time you press ENTER:", end='')
        while(True):
            input()
            print(currentTime(), end='')
    except KeyboardInterrupt:
        print("Done")
