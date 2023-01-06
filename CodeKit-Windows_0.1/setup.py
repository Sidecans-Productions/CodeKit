import os 
import time
import sys
import webbrowser
print("Welcome to the setup process of EasyAI")
time.sleep(0.6)
def gui():
    os.system('cls')
    print("Setup Program [1]")
    print("Credits[2]")
    print("Exit [3]")
    key = input()
    if key == "1":
        os.system('cls')
        webbrowser.open_new()
    elif key == "2":
        print("Client Dev: Sidecan")
        print("Front-End Dev: Cactus__ & hernan do")
        time.sleep(0.6)
        gui()
    elif key == "3":
        sys.exit()
    else:
        gui()
gui()


