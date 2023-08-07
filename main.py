from pytube import YouTube
import os
from sys import platform

destination="."
#This sofwtare is for EDUCATIONA PURSPOSE ONLY, the autho do not take any responsibility for your use, downloading youtube content is againts the copyright and against youtube terms

class txtcolors:
    ok='\033[92m'       #green
    fail='\033[91m'     #red
    reset='\033[0m'     #reset
    warn='\033[93m'     #yellow


def clear():
    if platform=="linux" or platform=="linux2":
            os.system("clear")
    elif platform=="win32":
            os.system("cls")

def Downloadmp3(video):

    flag=False

    video=video.streams.get_audio_only()

    print(txtcolors.warn+"\nAttempting to download: '"+video.title+".mp3'"+txtcolors.reset)
#    the following line is to allow you to save the file in a different directory
#    destination=str(input("")) or ('.')
    try:
        out_file=video.download(output_path=destination)
        base, ext=os.path.splitext(out_file)
        new_file=base+'.mp3'
        os.rename(out_file, new_file)
        clear()
    except:
        print(txtcolors.fail+"An error has occurred"+txtcolors.reset)
        flag=True

    if flag!=True:
        print(txtcolors.ok+"************************************")
        print("*Download is completed successfully*")
        print("************************************"+txtcolors.reset)


def Downloadmp4(video):
    flag=False

    video=video.streams.get_highest_resolution()

    print(txtcolors.warn+"\nAttempting to download: '"+video.title+".mp4'"+txtcolors.reset)

#    the following line is to allow you to save the file in a different directory
#    destination=str(input("")) or ('.')
    try:
        out_file=video.download(output_path=destination)
        base, ext=os.path.splitext(out_file)
        new_file=base+'.mp4'
        os.rename(out_file, new_file)
        clear()
    except:
        print(txtcolors.fail+"An error has occurred"+txtcolors.reset)
        flag=True

    if flag==False:
        print(txtcolors.ok+"************************************")
        print("*Download is completed successfully*")
        print("************************************"+txtcolors.reset)



while True:
    clear()
    link=input("Enter the YouTube video URL: ")
    video=YouTube(link)

    ext='.'
    while(ext!='mp3' and ext!='mp4'):
        ext=str(input("\nChoose what to download:\n>mp3<\n>mp4<\n\n"))

    if ext=="mp3":
        Downloadmp3(video)
    else:
        Downloadmp4(video)


    answer=str(input("\nDo you wanna download another file?\n"))
    if answer=='nope' or answer=='no' or answer=='No' or answer=='Nope':
        break;
    clear()


input("Have a nice day!")
clear()

