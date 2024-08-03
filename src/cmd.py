from src import art, downloader, txtcolors, file


def start():
    return


def new_path():
    txtcolors.clear()
    file.new_path()
    
    
def show_path():
    txtcolors.clear()
    print("The actual path is:\n\n\n>\t"+file.show_path()+"\t\t<")
    input("\n\nPress enter to go ahead\n>>>")
        
        
def new_res():
    txtcolors.clear()
    file.new_res()
        
       
def panic():
    while True:
        txtcolors.clear()
        res=input("Do you really want to restore all settings?\n\n>>>")
        if res=='1' or res=="yes" or res=="YES" or res=="Yes" or res=="y":
            file.panic()
            break
        break
            
               
def _exit():
    txtcolors.totcls()
    txtcolors.totcls()
    print(txtcolors.warn("Have a nice day!"))
    quit()
    
def get_command():
    ans=''
    txtcolors.clear()
    while ans!='m' and ans!='r' and ans!='p' and ans!='x' and ans!='s' and ans!='e':
        ans=input("Press 'm' to modify the path where the files are downloaded\nPress 'r' to modify the default resolution\nPress 'p' to show the current file download path\nPress 'x' to reset all the settings\nPress 's' to start the program\nPress 'e' to close the program\n\n>>>")
    
    if ans == 's':
        return True
        
    elif ans == 'm':
        new_path()
    
    elif ans == 'r':
        new_res()
        
    elif ans == 'p':
        show_path()
    
    elif ans == 'x':
        panic()
    
    elif ans == 'e':
        _exit()
        

    get_command()

