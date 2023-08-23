import time
#print(dir(time))
#name=input("Enter the name")
#print(name)
seconds=input("enter the time in number of seconds")
def counter(seconds):
    while seconds>0:
        mins=int(seconds/60)
        secs= int(seconds%60)
        timer=f'{mins}:{secs}'
        time.sleep(0.4)
        print(timer)
        seconds-=1
    print("timesup")
counter(int(seconds))