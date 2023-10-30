import json, string, random, os, time
from character import Player
from randomFunctions import clearTerminal
#levels
import levels.levIntro as lIntro

# global Player object
player = Player("")

# clears terminal screen

# reads json save file's contents into array of dict's
def loadSaveContent():
    try:
        f = open("TEXTBASEDADVENTURE/saves.json", "r")
        content = json.loads(f.read())
        f.close()
        return content
    except:
        return []
# load character into global player obj
def loadCharacter(nameLoad):
    content = loadSaveContent()
    for i in content:
        if "name" in i:
            if i["name"] == nameLoad:
                player.name = i["name"]
                player.level = i["level"]
                player.health = i["health"]
                player.maxHealth = i["maxHealth"]
                player.mana = i["mana"]
                player.maxMana = i["maxMana"]
                player.strength = i["strength"]
                player.defense = i["defense"]
                player.magic = i["magic"]
                player.magicDefense = i["magicDefense"]
                player.exp = i["exp"]
                player.expNeeded = i["expNeeded"]
                player.pClass = i["pClass"]
                player.inventory = i["inventory"]
                player.variables = i["variables"]
                #print(player.variables)
    clearTerminal()
    print(player)
# method to handle user input and loading of a character
def loadSaves():
    valid = False
    names = []
    # load the character saves file
    content = loadSaveContent()
    # Loop through characters print each name
    # First Check if any exist
    if len(content) > 0:
        for i in content:
            if "name" in i:
                print(i["name"])
                names.append(i["name"])
        while valid is False:
            print("Select a name to load, or type Quit to return.")
            nameLoad = input("Name: ").capitalize()
            if nameLoad in names:
                valid = True
            elif nameLoad == "Quit":
                gameStart()
    else:
        print('No Saves found, Press Enter to return')
        input('...')
        gameStart()
    # Send the name to loadCharacter method to load character into global player obj
    loadCharacter(nameLoad.capitalize())

def saveNewCharacter(newCharacter):
    x = 0
    # load saves, put in array, append new save to array, overwrite save file.
    content = loadSaveContent()
    saveArray = []
    saveArray.append(newCharacter.__dict__)
    length = len(content)
    while x < length:
        saveArray.append(content[x])#.__dict__)
        x += 1
    file = open("TEXTBASEDADVENTURE/saves.json", "w")
    data = json.dumps(saveArray, indent=4)
    file.write(data)
    file.close()

def newCharacter():
    print("Welcome weary traveler!")
    name = choose_name()
    Hero = Player("")
    Hero.name = name
    Hero.pClass, s, d, m, md = choose_class()
    Hero.strength += s
    Hero.defense += d
    Hero.magic += m
    Hero.magicDefense += md
    Hero.maxMana += 5 + (Hero.magic * 2)
    Hero.maxHealth += Hero.strength * 2
    Hero.mana = Hero.maxMana
    Hero.health = Hero.maxHealth
    # clear screen and show character info
    clearTerminal()
    print(f"Hero Card:")
    time.sleep(0.3)
    print(f"{Hero}")
    # confirm they want to save and continue to game or go back to menu
    print("Save new character?")
    i = input("Y or N").upper()
    if i == "Y":
        saveNewCharacter(Hero)
        #intro.init()

def gameStart():
    # Wipe the terminal clean, ask if user is new or returning
    clearTerminal()
    print("Welcome!")
    print("Please select whether you are returning or starting a new journey")
    choice = 0
    # Loop until they pick a valid choice
    while choice > 3 or choice < 1:
        print("1 = New, 2 = Resume, 3 = Quit")
        choice = int(input())
        clearTerminal()
    if choice == 3:
        os._exit(0)
    elif choice == 2:
        loadSaves()
        #print(player)
        hub()
    elif choice == 1:
        newCharacter()
        hub()

def choose_name():
    notAllowed = ["QUIT"]
    usedNames = []
    valid = False
    clearTerminal()
    # load saved files and grab names of character
    content = loadSaveContent()
    for i in content:
        if "name" in i:
            usedNames.append(i["name"])
    # ask for name, make sure name is valid, and name is not used
    while valid is False:
        print("Please enter your name:")
        name = input("Name: ")
        name_length = len(name)
        if name_length > 0:
            if name.upper() in notAllowed:
                print(f"The word {name} is not allowed")
                time.sleep(0.3)
                input("Press Enter to continue..")
                clearTerminal()
            elif name.capitalize() in usedNames:
                print(f"The name {name.capitalize()} is already in use")
                time.sleep(0.3)
                input("Press Enter to continue..")
                clearTerminal()
            else:
                valid = True
    return name.capitalize()
# for asking questions for stat points
def classStatQuestion(question,opt1,opt2):
    choice = 0
    while choice < 1 or choice > 2:
        clearTerminal()
        print(question)
        print(f'1 - {opt1}, 2 - {opt2}')
        choice = int(input())
    return choice

def choose_class():
    clearTerminal()
    notAllowedClasses = ["QUIT"]
    strengthClasses = ["FIGHTER", "KNIGHT", "DRAGOON"]
    magicClasses = ["MAGE", "SORCERER", "WITCH"]
    valid = False
    choice = 0
    pClass = ""
    strength = 0
    magic = 0
    defense = 0
    magDefense = 0
    choice = classStatQuestion('Would you rather Punch someone? Or Daydream of punching someone?','Punch','Daydream')
    if choice == 1:
        # return 'Fighter'
        strength += 1
    else:
        # return 'Mage'
        magic += 1
    choice = classStatQuestion("Would you rather kick a fool? Or kick a rock at them?",'Kick','Rocks')
    if choice == 1:
        strength += 1
    else:
        magic += 1
    choice = classStatQuestion('Would you rather Block a punch? Or Counter Attack?','Block','Counter')
    if choice == 1:
        defense == 1
    else:
        strength += 1
    choice = classStatQuestion("If someone kicked rocks at you would you try "+
        "to Absorb the damage or Kick Rocks back hoping to stop some",'Absorb','Reflect')
    if choice == 1:
        defense += 1
    else:
        magDefense += 1
    while valid is False:
        classWords = [] 
        print("Choose your own Class Name")
        print("Press enter to submit")
        pClass = input()
        classWords = pClass.split()
        if len(pClass) > 0:
            c = 0
            pClass = ''
            for x in classWords:
                c += 1
                if c > 1:
                    pClass += '-'
                pClass += x.capitalize()
                if x.upper() in magicClasses:
                    magic += 2
                    magDefense += 1
                    print('Magic Class Bonus')
                    time.sleep(.1)
                elif x.upper() in strengthClasses:
                    strength += 2
                    defense += 1
                    print('Strength Class Bonus')
                    time.sleep(.1)     
        valid = True
    return (pClass, strength, defense, magic, magDefense)

def afterCharacterSelect():
    print(f'What would you like to do {player.name}?')

# MAPS BELOW
def hub():
    global player
    #print("in hub")
    #print(player)
    if player.variables['levelIntro'] is True:
        player = lIntro.initIntroLevel(player)

gameStart()