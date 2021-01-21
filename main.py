import os

file = open("lol.txt", "r+")

while True:
    file.write("lol")
    os.system("git add .")
    file.close()
    os.system("git commit -m \"lol\"")
    file.write("XD")
    file = open("lol.txt", "r+")
    os.system("git add .")
    os.system("git commit -m \"XD\"")


file.close()
