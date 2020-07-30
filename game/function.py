import os

rows, columns = os.popen('stty size', 'r').read().split()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')