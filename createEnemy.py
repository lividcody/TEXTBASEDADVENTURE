import json, os, string
from enemy import Enemy


def clear_terminal():
    os.system("cls||clear")


def entry(varName):
    vari = input(f"Enter Enemy {varName}:\n\t")
    print(f"{varName} is {vari}")
    return vari


def multiEntry(varName):
    count = int(input(f"How many {varName}'s will you enter?\n\t"))
    cnt = count
    varis = []
    if count == 1:
        vari = entry(varName)
        varis.append(vari)
        return varis
    elif count == 0:
        return "None"
    while count > 0:
        count -= 1
        vari = input(f"Enter Enemy {varName} {count}:\n\t")
        varis.append(vari)
    print(f"{varName}'s are")
    while cnt > 0:
        print(f"\t{varis[cnt-1]}")
        cnt -= 1


def main():
    clear_terminal()
    f = open("TEXTBASEDADVENTURE/enemies.json", "r")
    content = json.loads(f.read())
    # print(content)
    enemyArray = []
    length = len(content)
    # print(length)
    x = 0
    while x < length:
        enemyArray.append(content[x])
        x += 1
    for i in content:
        if "name" in i:
            print(i["name"])
    # FIGURE OUT HOW TO ACCESS THIS DICT, this loop could be used to search through etc use json id "id"
    enterMore = "Y"
    while enterMore == "Y":
        name = entry("Name")
        level = entry("Level")
        desc = entry("Description")
        health = entry("Health")
        strength = entry("Strength")
        magic = entry("Magic")
        defense = entry("Defense")
        magDefense = entry("Magic Defense")
        weakness = multiEntry("Weakness")

        # enemy = Enemy(name,level,desc,health,strength,magic,defense,magDefense,weakness)

        enemyDictionary = dict(
            name=name,
            level=level,
            desc=desc,
            health=health,
            strength=strength,
            magic=magic,
            defense=defense,
            magDefense=magDefense,
            weakness=weakness,
        )
        enemyArray.append(enemyDictionary)
        i = askMore()
        enterMore = i
    file = open("TEXTBASEDADVENTURE/enemies.json", "w")
    data = json.dumps(enemyArray, indent=4)
    file.write(data)
    file.close()


def askMore():
    clear_terminal()
    print("Enter more Enemies?")
    i = input("Y or N")
    return i.upper()


main()
