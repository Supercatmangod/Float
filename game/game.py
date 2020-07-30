import json
import colorama
import time
from function import cls 
import os

CurrentRoom = "wasteland"
Inventory = []

map = {
    "Wasteland" : {
        "info":"Empty land for miles and miles.",
        "north":"Wasteland",
        "south":"Wasteland",
        "east":"Frumentum",
        "items":{
            "apple":None,
            "orange":None
        }
    },
    "Frumentum":{
        "info":"The largest city on earth and the city with all of the war toys"        
    
        }
}

def die():
    cls()
    print()
    print("You Died :(")
    print()
    input()
    exit(0)
    


def gamefunction(GameInfo,PlayerInfo,DebugInfo,rows, columns):


    print("Loading...")

    time.sleep(0.5);
    cls()
    CurrentRoom = "Wasteland"
    while True:
        #gamemod.update();
        def showInfo():
            print("=========")
            print(colorama.Fore.MAGENTA,end='')
            print("Current Room: " + CurrentRoom)
            print(colorama.Fore.GREEN,end='')
            print("Room Info: " + map[CurrentRoom]["info"])
            print(colorama.Fore.YELLOW,end='')
            try:
                print("Items In Room: " + str(list(map[CurrentRoom]["items"])))
            except:
                print(end='')
            print(colorama.Fore.CYAN,end='')
            print("Inventory: " + str(Inventory))
            print(colorama.Fore.RESET,end='')
            print("=========")
        showInfo()
        print(">",end='')
        command = input().lower().split()
        try:
            if command[0] == "go":
                if command[1] == "north":
                    CurrentRoom = map[CurrentRoom]["north"]
                if command[1] == "south":
                    CurrentRoom = map[CurrentRoom]["south"]
                if command[1] == "east":
                    CurrentRoom = map[CurrentRoom]["east"]
                if command[1] == "west":
                    CurrentRoom = map[CurrentRoom]["west"]
        except:
            print()
            print("You Cant Go That Way")
            print()
        try:
            if command[0] == "look":
                if command[1] == "around":
                    print()
                    print(str(map[CurrentRoom]["info"]))
                    print()
                    if "north" in map[CurrentRoom]:
                        print("To the north is: " + map[CurrentRoom]["north"])
                    if "south" in map[CurrentRoom]:
                        print("To the south is: " + map[CurrentRoom]["south"])
                    if "east" in map[CurrentRoom]:
                        print("To the east is: " + map[CurrentRoom]["east"])
                    if "west" in map[CurrentRoom]:
                        print("To the west is: " + map[CurrentRoom]["west"])
                    print()
            if command[0] == "grab":
                if(command[1] in map[CurrentRoom]["items"]):
                    Inventory.append(command[1])
                    del map[CurrentRoom]["items"][command[1]]
                    #map[CurrentRoom].update({"items" : {}}) 
                    print("")
                    print("You Grabed The: " + command[1])
                else:
                    print("You Can't Grab Somthing That Is Not There")
            if command[0] == "drop":
                if(command[1] in Inventory):
                    try:
                        map[CurrentRoom]["items"].update({command[1] : None})
                    except:
                        map[CurrentRoom].update({"items" : {}})
                        map[CurrentRoom]["items"].update({command[1] : None})
                    Inventory.remove(command[1])
                    print("")
                    print("You Droped The: " + command[1])
            if command[0] == "exit":
                print("Closing Game...")
                #del map
                #del CurrentRoom
                #del command
                #del Inventory
                print("Do You Want to Leave?")
                print('[y:N]:',end='')
                if(input().lower == 'y'):
                    #time.sleep(1)
                    exit(0)
            if command[0] == "menu":
                if(DebugInfo["devmenu"] == "yes"):
                    cls()
                    print("Development Menu".center(int(columns),'='))
                    print("[A]: Run Command")
                    print("[B]: Show Map")
                    print("[C]: Show Inventory")
                    print("[D]: Python Input")
                    print("[E]: Load Mod")
                    print(">" ,end='')
                    del command
                    command = input().lower()
                    if command == 'a':
                        print(">",end='')
                        codecommand = input()
                        eval(str(codecommand))
                    if command == 'b':
                        print(str(list(map)))
                    if command == 'c':
                        print(str(Inventory))  
                    if command == 'd':
                        os.system("python3")
                    if command == 'e':
                        try:
                            eval(open("mods/mod.py").read())
                        except:
                            print("No Mod Found Please Put 'mod.py' in to the mod folder")
        except:
            print("ERROR");        
        