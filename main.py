from pytube import YouTube
import os
from sys import platform

def space():
    for i in range(5):
        print("\n")

def clear():
    if platform=="linux" or platform=="linux2":
            os.system("clear")
    elif platform=="win32":
            os.system("cls")

def Download(link):
    ext='.'
    while(ext!='mp3' and ext!='mp4'):
        ext=str(input("\nChoose what to download:\n>mp3<\n>mp4<\n\n"))

    flag=False
    video = YouTube(link)
#   Download as mp3
    if ext=='mp3':
        destination='.'
        video=video.streams.get_audio_only()
        print("Attempting to download: '"+video.title+".mp3'")

#       the following line is to allow you to save the file in a different directory
#       destination=str(input("")) or ('.')

        try:
            out_file=video.download(output_path=destination)
            base, ext=os.path.splitext(out_file)
            new_file=base+'.mp3'
            os.rename(out_file, new_file)
            clear()
        except:
            print("An error has occurred")
            flag=True

        if flag!=True:
            print("Download is completed successfully")


#   download as mp4
    else:
        video = video.streams.get_highest_resolution()
        print("Attempting to download: '"+video.title+".mp4'")
        try:
            video.download()
            clear()

        except:
            print("An error has occurred")
            flag=True
        if flag==False:
            print("Download is completed successfully")




while True:
    clear()
    link = input("Enter the YouTube video URL: ")
    Download(link)
    answer=str(input("\nDo you wanna download other file?\n"))
    if answer=='nope' or answer=='no' or answer=='NO' or answer=='Nope':
        break;
    clear()


input("Have a nice day!")
