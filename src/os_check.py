from sys import platform as plt

def check_os():
    if plt == 'darwin':
        return 'darwin'
 
    elif plt == 'linux':
        return 'linux'
 
    elif plt == 'win32':
        return 'win32'
        
def is_darwin():
    if plt == 'darwin':
        return True
    return False
    
def is_win32():
    if plt == 'win32':
        return True
    return False
    
def is_linux():
    if plt == 'linux':
        return True
    return False
