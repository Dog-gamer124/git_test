import os
import time

file = open("lol.txt", "a")
n=0
try:
    while True:
        file.write("")
        file.close()
        file = open("lol.txt", "a")
        os.system("git add .")
        os.system("git commit -m \"XD\"")
        n+=1
except KeyboardInterrupt:
    print(n)
    


file.close()
