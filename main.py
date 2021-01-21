import os
import time

file = open("lol.txt", "a")
n=0
try:
    while True:
        file.write("a")
        file.close()
        file = open("lol.txt", "a")
        os.system("git add .")
        #time.sleep(1)
        os.system("git commit -m \"XD\"")
        n+=1
except KeyboardInterrupt:
    print(n)
    


file.close()
