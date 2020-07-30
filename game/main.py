#/bin/python3

#Import libarys
import json
import colorama 
from function import cls
import os
from game import gamefunction

#Get console things
rows, columns = os.popen('stty size', 'r').read().split()

#Temp value
temp = open("./config/game.json","r").read()

#Get json data
maininfo = json.loads(temp)

#Delete Temp
del temp

#OPen Dubug
temp = open("./config/debug.json","r").read()

debuginfo = json.loads(temp)

#Player Object
Player = {
    "name": maininfo["player"]["name"],
    "age": maininfo["player"]["age"],
    "sex": maininfo["player"]["sex"]
}

#GameInfo Object
Game = {
    "name": maininfo["game"]["info"]["name"],
    "version": maininfo["game"]["info"]["version"],
    "creator": maininfo["game"]["info"]["creator"],
    "title": {
        "text": maininfo["game"]["title"]["text"]
    }
}

#Enable Colored Text
colorama.init()

#Functions
def ShowTitle():
    titlebar = "="
    for i in range(int(columns) - 1):
        titlebar = titlebar + "="
    print(titlebar)
    title = str(Game["title"]["text"])
    version = "Version " + str(Game["version"])
    creator = str(Game["creator"])
    print(title.center(int(columns) , ' '))
    print(colorama.Fore.CYAN,end='') 
    print(version.center(int(columns) , ' '))
    print(colorama.Fore.RED)
    print("Created By".center(int(columns),' '))
    print(colorama.Fore.GREEN,end='')
    print(creator.center(int(columns), ' '))
    print(colorama.Fore.RESET,end='')
    print(titlebar)

#Clear Console
cls()

if debuginfo["skiptitle"] == "no":
    #Game Code
    ShowTitle()
    print("Press Enter To Read Prologue.")
    input()
    print("Prologue:")
    temp = str(open("./prologue.txt","r").read())
    print()
    print(temp.replace("{name}",str(Player["name"])))
    del temp
    print("Press Enter To Play The Game.")
    input()

#Run Game Code
gamefunction(Game,Player,debuginfo,rows, columns);