import os

def path():
    file=open("path.txt",'r')
    path=file.read()
    file.close()
    
    if path=='':
        return '.'
    return path


def new_path():
    path = open("path.txt",'w')
    path.write(input("Insert the path (if you don't know press '.'):\n\n>>>"))
    path.close()

def show_path():
    file=open("path.txt", 'r')
    path=file.read()
    file.close()
    return path
    
        
def is_res():
    file=open("resolution.txt",'r')
    res=file.read()
    file.close()
    
    if res=='2' or res=='lowest' or res=='Lowest' or res=='LOWEST':
        return True
    return False
    
def new_res():
    file=open("resolution.txt",'w')
    file.write(input("Insert the designated resolution (default to Highest):\n> Highest avaible\n> Lowest avaible\n\n>>>"))
    file.close()

    
