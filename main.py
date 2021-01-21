import os

file = open("lol.txt", "a")
n=0

while True:
    file.write("lol")
    os.system("git add .")
    #os.system("git commit -m \"lol\"" )
    file.write("XD")
    os.system("git add .")
    os.system("git commit -m \"XD\"")
    n+=1


file.close()
