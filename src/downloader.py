from pytube import YouTube
from pytube import Playlist
import os
from pydub import *
from src import txtcolors
from src import path

list=[]
def _path():
    file=open("path.txt",'r')
    path=file.read()
    file.close()
    
    if path=='':
        return '.'
    return path

#printing total error while downloading
def toterr():
    num=0
    print("The number of error is: "+txtcolors.fail(str(len(list))))
    if len(list)>0:
        print(txtcolors.warn("The following video has not been downloaded:\n"))
        for x in list:
            num=num+1
            print(str(num)+") "+x)

def convert(toconvert, path):
    video=AudioSegment.from_file(toconvert, format="mp4")
    video.export(path, format="mp3")
    

def Downloadmp3(video):
    print(txtcolors.warn("Attempting to download: '"+video.title+".mp3'"))

#    the following line is to allow you to save the file in a different directory
#    _path=str(input("")) or ('.')
    try:
        video=video.streams.get_audio_only()
        out_file=video.download(output_path=path.path())            #download the video
        base, ext=os.path.splitext(out_file)
        new_file=base+'.mp4'                                    #this is the mp4 file path
        mp3path=base+'.mp3'                                     #this is the mp3 file path
        os.rename(out_file, new_file)
        
        convert(new_file, mp3path)
                              #this is needed to convert the file from mp4 to mp3
        os.remove(new_file)
                                         #this one delete the mp4 file
        txtcolors.clear()
        print(txtcolors.ok("Download of: '"+video.title+"' is completed successfully"))

    except:
        print(txtcolors.fail("An error has occurred, download of: '"+video.title+"' has failed"))
        list.insert(0, video.title)

def Downloadmp4(video):
    print(txtcolors.warn("Attempting to download: '"+video.title+".mp4'"))

    try:
        video=video.streams.get_highest_resolution()

        out_file=video.download(output_path=path.path())
        base, ext=os.path.splitext(out_file)
        new_file=base+'.mp4'
        os.rename(out_file, new_file)
        txtcolors.clear()
        print(txtcolors.ok("Download of: '"+video.title+"' is completed successfully"))

    except:
        print(txtcolors.fail("An error has occurred, download of: '"+video.title+"' has failed"))
        list.insert(0, video.title)
