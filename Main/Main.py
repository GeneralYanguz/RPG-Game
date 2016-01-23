from time import sleep
import sys, pickle, random
def savegame():
    file = open(p_name + ".txt", 'wb')
    pickle.dump(p_stats, file)
    file.close()
    print("Saved game")
    global p_position
    p_position += 1
    print("Do you want to continue playing or do you want to quit? continue/quit")
    continuegame = input(">").lower()
    if (continuegame == "continue") or (continuegame == "1"):
        if p_position == 1:
            prologue()
        #Add more places here!
    elif (continuegame == "quit") or (continuegame == "2"):
        sys.exit()
    else:
        print("That's not an option!")
        savegame()
def loadgame():
    print("What's the name of your savefile?(Your character name)")
    p_name = input(">")
    file = open(p_name + ".txt", 'rb')
    p_stats = pickle.load(file)
    print("Game loaded")
    if p_stats["p_position"] == 1:
        prologue()
    #Add more places here!
def start():
    gameon = True
    if gameon == True:
        print("***********************************")
        print("****  >>>A normal RPG game<<<  ****")
        print("****         By Yanguz         ****")
        print("****       1. New game         ****")
        print("****       2. Continue         ****")
        print("****       3. Exit             ****")
        print("***********************************")
    menuchoice = input(">")
    if menuchoice == "1":
        getinfo()
    elif menuchoice == "2":
        loadgame()
    elif menuchoice == "3":
        print("Are you sure you want to quit? Y/N")
        quit1 = input(">")
        quit1 = quit1.upper()
        if quit1 == "Y":
            sys.exit()
        elif quit1 == "N":
            print("Wow, you scared me there:)")
            start()
    else:
        print("I don't understand...")
        start()
def getinfo():
    print("Hello! What's your name?")
    global p_name
    p_name = input(">").lower()
    if p_name in "nisse":
        print("You are not allowed to play this game!")
        sys.exit()
    elif p_name in "yanguz":
        print("You are cool")
        getinfo2()
    else:
        getinfo2()
def getinfo2():
    print("Choose your class:")
    print("Warrior: A might knight who swings a big sword")
    print("Mage: A magical user who uses a little staff")
    print("Barbarian: Throws big metal axes at his enemy's")
    global p_class
    p_class = input(">").lower()
    if p_class == "warrior":
        print("You chose the mighty warrior!")
        confirmclass()
    elif p_class == "mage":
        print("You chose the magical mage!")
        confirmclass()
    elif p_class == "barbarian":
        print("You chose the barbaric barbarian!")
        confirmclass()
    else:
        print("That's not a option!")
        getinfo2()


def confirmclass():
    print("Do you really want to be a " + p_class + "? y/n")
    global p_health, p_damage
    classconfirm = input(">").lower()
    if classconfirm == "y" or classconfirm == "yes":
        print("Nice! Let's start!")
        if p_class == "warrior":
            p_health = 15
            p_damage = random.randint(0,5)
            prologuebegin()
        elif p_class == "mage":
            p_health = 10
            p_damage = random.randint(0,7)
            prologuebegin()
        elif p_class == "barbarian":
            p_health = 20
            p_damage = random.randint(0,3)
            prologuebegin()
    elif classconfirm == "n" or classconfirm == "no":
        getinfo2()
    else:
        print("That's not a option!")
        confirmclass()
def prologuebegin():
    global p_position
    p_position = 0
    global p_stats
    p_stats = {"p_name": p_name,
               "p_class": p_class,
               "p_health": p_health,
               "p_damage": p_damage,
               "p_position": p_position}
    savegame()
def prologue():
    print("Done")
start()