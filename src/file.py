import os
to_path = "path.txt"
to_res = "resolution.txt"


def read(path):
    file = open(path,'r')
    doc = file.read()
    file.close()
    
    return doc
   
   
def write(path, ins):
    file = open(path, 'w')
    file.write(ins)
    file.close()
    
    
def path():
    path = read(to_path)
    
    if path=='':
        return '.'
    return path


def new_path():
    path = write(to_path, input("Insert the path (if you don't know press '.'):\n\n>>>"))


def show_path():
    return read(to_path)
    
        
def is_res():
    res = read(to_res)
        
    if res=='2' or res=='lowest' or res=='Lowest' or res=='LOWEST':
        return True
    return False
    
def new_res():
    write(to_res, input("Insert the designated resolution (default to Highest):\n> Highest avaible\n> Lowest avaible\n\n>>>"))
    

def panic():
    write(to_path, '.')
    write(to_res, '.')


def panic(val):
    if val==1:
        write(to_path, '.')
    
    if val==2:
        write(to_res, '.')


def verify():
    try:
        read(to_path)
    except:
        panic(1)
    
    try:
        read(to_res)
    except:
        panic(2)
        
