from randomFunctions import *
from character import Player


player = Player('')

def initIntroLevel(iPlayer):
    player = iPlayer
    introLevel()

def introLevel():
    introMsg()
    introSearch()

def introMsg():
    enterToContinue()
    clearTerminal()
    print("You start to open your eyes...")
    txtPause()
    print("You sit up in a daze...")
    txtPause()
    print("Looking around in a blur you realize this isnt your room.")
    txtPause()
    print("This definitely isn't your bed either, though it is soft.")
    txtPause()
    print("As your eyes start to focus you really take a look around")
    txtPause()
    enterToContinue()

def introSearch():
    inRoom = True
    desc = []
    desc.append('You stand in a small dimly lit room with 4 walls')
    desc.append('Theres a door in the wall to the North, ')
    desc.append('Theres a bookshelf to the East littered with books')
    desc.append('To the South is a desk littered with random papers')
    desc.append('To the West lies the bed you woke up on')
    
    while inRoom:
        i = ""
        i = input('What would you like to do?: ').upper()
        print('\n')
        if i == 'LOOK':
            print('You look around..\n')
            txtPause()
            printDesc(desc)
        
    
    
    