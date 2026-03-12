import time
import os


def countdown_timer(seconds):
    while seconds>0:
        mins = int(seconds/60)
        scnds = int(seconds%60)
        
        if scnds <10:
            scnds = f'0{scnds}'

        timer = f'{mins} : {scnds}'
        

        print (timer,end='\r')
        time.sleep(1)
        seconds-=1
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!TIME IS UPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    os.system("afplay scream_chicken_tree.wav")


    

#135 = 135/60 = 2minutes 15seconds




seconds = int(input("Enter the time in seconds: "))
countdown_timer(seconds)