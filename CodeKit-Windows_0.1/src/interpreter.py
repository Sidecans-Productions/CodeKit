import os
def interpret(file):
    languages = {"bas":"BASIC"}
    languagesstr = ("BASIC")
    extension = file.split(".")[1]
    os.system('cls')
    print("File Selected: " + file)
    print("Detected Language: " + languages[extension])
    print("Continue[1]")
    #print("Manually Select[2]")
    key = input()
    if key == "1":
        os.system('cls')
        selected = languages[extension]


        