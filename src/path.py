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
