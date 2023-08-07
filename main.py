from pytube import YouTube
from pytube import Playlist
import os
from sys import platform

destination="."
list=[]

#This sofwtare is for EDUCATIONAl PURSPOSE ONLY, the autho do not take any responsibility for your use, downloading youtube content is againts the copyright and against youtube terms

class txtcolors:
    ok='\033[92m'       #green
    fail='\033[91m'     #red
    reset='\033[0m'     #reset
    warn='\033[93m'     #yellow

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
    if platform=="linux" or platform=="linux2":
            os.system("clear")
    elif platform=="win32":
            os.system("cls")

def pl():
    p=Playlist(input("Enter Youtube playlist URL: "))
    y="."
    while y!="mp3" and y!="mp4":
        y=str(input("Choose how to download:\n>mp3<\n>mp4<\n\n"))

    clear()
    if y=="mp3":
        for url in p.video_urls:
            video=YouTube(url)
            Downloadmp3(video)
    else:
        for url in p.video_urls:
            video=YouTube(url)
            Downloadmp4(video)

def video():
    link=input("Enter the YouTube video URL: ")
    video=YouTube(link)

    ext='.'
    while(ext!='mp3' and ext!='mp4'):
        ext=str(input("\nChoose how to download:\n>mp3<\n>mp4<\n\n"))

    clear()
    if ext=="mp3":
        Downloadmp3(video)
    else:
        Downloadmp4(video)


def Downloadmp3(video):

    flag=False

    video=video.streams.get_audio_only()

    print(txtcolors.warn+"Attempting to download: '"+video.title+".mp3'"+txtcolors.reset)
#    the following line is to allow you to save the file in a different directory
#    destination=str(input("")) or ('.')
    try:
        out_file=video.download(output_path=destination)
        base, ext=os.path.splitext(out_file)
        new_file=base+'.mp3'
        os.rename(out_file, new_file)
        clear()
    except:
        print(txtcolors.fail+"An error has occurred, download of: '"+video.title+"' has failed"+txtcolors.reset)
        list.insert(0, video.title)
        flag=True

    if flag!=True:
   #     print(txtcolors.ok+"************************************")
        print(txtcolors.ok+"Download of: '"+video.title+"' is completed successfully"+txtcolors.reset+"\n")
 #       print("************************************"+txtcolors.reset)


def Downloadmp4(video):
    flag=False

    video=video.streams.get_highest_resolution()

    print(txtcolors.warn+"Attempting to download: '"+video.title+".mp4'"+txtcolors.reset)

#    the following line is to allow you to save the file in a different directory
#    destination=str(input("")) or ('.')
    try:
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



while True:
    clear()

    x="."
    while x!="video" and x!="playlist" and x!="Video" and x!= "Playlist" and x!="pl":
        x=str(input("Do you wanna download a video or a playlist?"))

    clear()
    if x=="video" or x=="Video":

        video()
    else:
        pl()

    clear()
    toterr()

    answer=str(input("\nDo you wanna download another file?\n"))
    if answer=='nope' or answer=='no' or answer=='No' or answer=='Nope':
        break;
    clear()


input(txtcolors.warn+"\n\nHave a nice day!"+txtcolors.reset)
clear()
