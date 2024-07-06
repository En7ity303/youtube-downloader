from pytube import YouTube
from pytube import Playlist
import os
from sys import platform
from pydub import *

destination="/Users/giorgio/documents/coding/script/musica"
list=[]

#This sofwtare is for EDUCATIONAl PURSPOSE ONLY, the author do not take any responsibility for your use, downloading youtube content is againts the copyright and against youtube terms

class txtcolors:
    ok='\033[92m'       #green
    fail='\033[91m'     #red
    reset='\033[0m'     #reset
    warn='\033[93m'     #yellow
    header='\033[95m'   #purple
    cyan='\033[96m'     #cyan

def welcome():

    resp=str(input(txtcolors.warn+"\n\nDownloading YouTube video is against copyright and YouTube terms, do you wanna continue? If go ahead the author do not take any responsibility for your usage\n\n>>>"+txtcolors.reset))

    if resp!="yes" and resp!="Yes":
        quit()
        
#printing total error while downloading
def toterr():
    num=0
    print("The number of error is: "+txtcolors.fail+str(len(list))+txtcolors.reset)
    if len(list)>0:
        print(txtcolors.warn+"The following video has not been downloaded:\n")
        for x in list:
            num=num+1
            print(str(num)+") "+x)
        print(txtcolors.reset)

def clear():
    if platform=="linux" or platform=="linux2" or platform=="darwin":
            os.system("clear")
    elif platform=="win32":
            os.system("cls")

def pl():
    p=Playlist(input("Enter Youtube playlist URL: \n>>>"))
    y="."
    while y!="mp3" and y!="mp4":
        y=str(input("Choose how to download:\n>mp3<\n>mp4<\n\n>>>"))

    clear()
    if y=="mp3":
        for url in p.video_urls:
            video=YouTube(url)
            Downloadmp3(video)
    if y=="mp4":
        for url in p.video_urls:
            video=YouTube(url)
            Downloadmp4(video)

def video():
    link=input("Enter the YouTube video URL: \n>>>")
    video=YouTube(link)

    ext='.'
    while(ext!="mp3" and ext!="mp4" and ext!="1" and ext!="2"):
        ext=str(input("\nChoose how to download:\n>mp3<\n>mp4<\n\n>>>"))

    clear()
    if ext=="mp3" or ext=="1":
        Downloadmp3(video)
    if ext=="mp4" or ext=="2":
        Downloadmp4(video)

def convert(toconvert, path):
    video=AudioSegment.from_file(toconvert, format="mp4")
    video.export(path, format="mp3")
    

def Downloadmp3(video):

    flag=False
    print(txtcolors.warn+"Attempting to download: '"+video.title+".mp3'"+txtcolors.reset)

#    the following line is to allow you to save the file in a different directory
#    destination=str(input("")) or ('.')
    try:
        video=video.streams.get_audio_only()
        out_file=video.download(output_path=destination)        #download the video
        base, ext=os.path.splitext(out_file)
        new_file=base+'.mp4'                                    #this is the mp4 file path
        mp3path=base+'.mp3'                                     #this is the mp3 file path
        os.rename(out_file, new_file)
        convert(new_file, mp3path)                              #this is needed to convert the file from mp4 to mp3
        os.remove(new_file)                                     #this one delete the mp4 file
        clear()
    except:
        print(txtcolors.fail+"An error has occurred, download of: '"+video.title+"' has failed"+txtcolors.reset)
        list.insert(0, video.title)
        flag=True

    if flag==False:
   #     print(txtcolors.ok+"************************************")
        print(txtcolors.ok+"Download of: '"+video.title+"' is completed successfully"+txtcolors.reset+"\n")
 #       print("************************************"+txtcolors.reset)


def Downloadmp4(video):
    flag=False
    print(txtcolors.warn+"Attempting to download: '"+video.title+".mp4'"+txtcolors.reset)

#    the following line is to allow you to save the file in a different directory
#    destination=str(input("")) or ('.')
    try:
        video=video.streams.get_highest_resolution()
        out_file=video.download(output_path=destination)
        base, ext=os.path.splitext(out_file)
        new_file=base+'.mp4'
        os.rename(out_file, new_file)
        clear()
    except:
        print(txtcolors.fail+"An error has occurred, download of: '"+video.title+"' has failed"+txtcolors.reset)
        list.insert(0, video.title)
        flag=True

    if flag==False:
#        print(txtcolors.ok+"************************************")
        print(txtcolors.ok+"Download of: '"+video.title+"' is completed successfully"+txtcolors.reset+"\n")
#        print("************************************"+txtcolors.reset)


welcome()
print(txtcolors.header+"Welcome in YouTube Downloader\n\n\n"+txtcolors.reset)
flag_pl=False
while True:
    clear()
    x="."
    while x!="video" and x!="playlist" and x!="Video" and x!= "Playlist" and x!="pl" and x!="vd" and x!="1" and x!="2":
        x=str(input("Choose the format you wanna download:\n>Video<\n>Playlist<\n\n>>>"))
    clear()
    
    while True:
        if x=="video" or x=="Video" or x=="vd" or x=="1":
            video()
            ans=input("\nDo you wanna download another video?\n>>>")
            if ans=='nope' or ans=='no' or ans=='No' or ans=='Nope' or ans=='nop':
                break
            clear()
    
    if x=="Playlist" or x=="playlist" or x=="pl" or x=="2":
        pl()
        flag_pl=True

    if flag_pl==True:
        clear()
        toterr()

    break
    clear()


input(txtcolors.warn+"\n\nHave a nice day!"+txtcolors.reset)
clear()
