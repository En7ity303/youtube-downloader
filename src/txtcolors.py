from sys import platform as plt
import os
from src import art

class col:
    ok='\033[92m'       #green
    fail='\033[91m'     #red
    reset='\033[0m'     #reset
    warn='\033[93m'     #yellow
    header='\033[95m'   #purple
    cyan='\033[96m'     #cyan


def ok(str):
    print(col.ok + str +col.reset)
    return''
    
def fail(str):
    print(col.fail + str + col.reset)
    return''
    
def warn(str):
    print(col.warn + str + col.reset)
    return ''
    
def header(str):
    print(col.header + str + col.reset)
    return''
    
def cyan():
    print(col.cyan + str + col.reset)
    return''
    
def clear():
    if plt=="linux" or plt=="linux" or plt=="darwin":
        os.system("clear")
    elif plt=="win32":
        os.system("cls")
        
    print(warn(art.art))
    return''
    
def totcls():
    if plt=="linux" or plt=="linux" or plt=="darwin":
        os.system("clear")
    elif plt=="win32":
        os.system("cls")
        
    return''
