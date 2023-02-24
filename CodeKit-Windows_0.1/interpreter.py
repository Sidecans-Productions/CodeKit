import os
from AI import AI
def interpret(file):
    
    os.system('cls')
    print("File Selected: " + file)
   
    print("Continue[1]")
    #print("Manually Select[2]")
    key = input()
    if key == "1":
        os.system('cls')
        with open(file, "r+") as f:
            dat = f.read()
            print(dat)
            newdat = dat.split("\n")
            print(newdat)
            AI.runAI(newdat)
           





                





        