from pytube import YouTube
from pytube import Playlist
import os
from sys import platform
from pydub import *
from src import art
from src import downloader
from src import txtcolors
from src import file

#This sofwtare is for EDUCATIONAl PURSPOSE ONLY, the author do not take any responsibility for your use, downloading youtube content is againts the copyright and against youtube terms

      


def disc():
    print(txtcolors.warn("\n\nDownloading YouTube video is against copyright and YouTube terms, do you wanna continue? If you go ahead the author of this tool does not take any responsibility for your usage"))
    resp=input(">>>")
    if resp!="YES" and resp!="Yes" and resp!="yes":
        quit()
        
def clear():
    if platform=="linux" or platform=="linux2" or platform=="darwin":
            os.system("clear")
    elif platform=="win32":
            os.system("cls")
            
    print(txtcolors.warn(art.art))


def pl():
    p=Playlist(input("Enter the YouTube playlist URL: \n>>>"))
    y='.'
    txtcolors.clear()
    while y!="mp3" and y!="mp4" and y!="1" and y!="2":
        y=str(input("Choose the format you wanna to download in:\n>mp3<\n>mp4<\n\n>>>"))

    txtcolors.clear()
    if y=="mp3" or y=="1":
        for url in p.video_urls[:3]:
            print(url)
            video=YouTube(url)
            downloader.Downloadmp3(video)
            
    if y=="mp4" or y=="2":
        for url in p.video_urls[:3]:
            video=YouTube(url)
            downloader.Downloadmp4(video)

def video():
    link=input("Enter the YouTube video URL: \n>>>")
    video=YouTube(link)

    ext='.'
    txtcolors.clear()
    while(ext!="mp3" and ext!="mp4" and ext!="1" and ext!="2"):
        ext=str(input("Choose the format you wanna to download in\n>mp3<\n>mp4<\n\n>>>"))

    txtcolors.clear()
    if ext=="mp3" or ext=="1":
        downloader.Downloadmp3(video)
    if ext=="mp4" or ext=="2":
        downloader.Downloadmp4(video)

##  MAIN  ##
disc()
flag_pl=False

while True:
    while True:
        txtcolors.clear()
        ans=input("Press 'm' to modify the path where the files are downloaded\nPress 'r' to modify the default resolution\nPress 'p' to show the current file download path\nPress 'x' to reset all the settings\nPress 's' to start the program\nPress 'e' to close the program\n\n>>>")

        if ans=='m':
            txtcolors.clear()
            file.new_path()
        
        elif ans=='p':
            txtcolors.clear()
            print("The actual path is:\n\n\n>\t"+file.show_path()+"\t\t<")
            input("\n\nPress enter to go ahead\n>>>")
        
        elif ans=='r':
            txtcolors.clear()
            file.new_res()
        
        elif ans=='x':
            while True:
                txtcolors.clear()
                res=input("Do you really want to restore all settings?\n\n>>>")
                if res=='1' or res=="yes" or res=="Yes" or res=="YES" or res=="y":
                    file.panic()
                    break
                break
        
        elif ans=='s':
            break
            
        elif ans=='e':
            txtcolors.totcls()
            input(txtcolors.warn("Have a nice day!"))
            txtcolors.totcls()
            quit()


    x="."
    while x!="video" and x!="playlist" and x!="Video" and x!= "Playlist" and x!="pl" and x!="vd" and x!="1" and x!="2":
        txtcolors.clear()
        x=str(input("Choose what you wanna download:\n>Video<\n>Playlist<\n\n>>>"))

    txtcolors.clear()
    while True:
        if x=="video" or x=="Video" or x=="vd" or x=="1":
            video()
            ans=input("\nDo you wanna download another video?\n>>>")
            if ans=='nope' or ans=='no' or ans=='No' or ans=='Nope' or ans=='nop':
                break
            txtcolors.clear()
    
        if x=="Playlist" or x=="playlist" or x=="pl" or x=="2":
            pl()
            flag_pl=True

        if flag_pl==True:
            txtcolors.clear()
            downloader.toterr()

        break
    txtcolors.clear()
