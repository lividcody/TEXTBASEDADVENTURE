import os, time


def clearTerminal():
    os.system("cls||clear")


def txtPause():
    time.sleep(0.5)


def enterToContinue():
    input("\nPress Enter to Continue\n")

def printDesc(descArray):
    for a in descArray:
        print(a)
        txtPause()
    print('\n')