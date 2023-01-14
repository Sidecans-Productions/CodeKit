import os
def interpret(file):
    languages = {"bas": "BASIC", "c": "C"}
    extensionsa = file.split(".")
    extension = extensionsa[2]
    print(extensionsa)
    os.system('cls')
    print("File Selected: " + file)
    print("Detected Language: " + str(languages[extension]))
    print("Continue[1]")
    #print("Manually Select[2]")
    key = input()
    if key == "1":
        os.system('cls')
        selected = languages[extension]
        if selected == "C":
            with open(file, "r+") as f:
                contents = f.readlines()
                x = len(f.readlines())
                x+= 1




        