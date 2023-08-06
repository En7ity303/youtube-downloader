from pytube import YouTube
import os

def space():
    for i in range(5):
        print("\n")


def Download(link):
    ext='.'
    while(ext!='mp3' and ext!='mp4'):
        ext=str(input("\nChoose what to download:\n>mp3<\n>mp4<\n\n"))

    flag=False
#   Download as mp3
    if ext=='mp3':
        videomp3 = YouTube(link)
        videomp3 = videomp3.streams.get_audio_only()
        print("Attempting to download: '"+videomp3.title+".mp3'")

#       the following line is to allow you to save the file in a different directory
#       destination=str(input("")) or ('.')

        destination='.'

        try:
            out_file = videomp3.download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            os.system("clear")
        except:
            print("An error has occurred")
            flag=True

        if flag!=True:
            print("Download is completed successfully")
#   download as mp4
    else:
        videomp4 = YouTube(link)
        videomp4 = videomp4.streams.get_highest_resolution()
        print("Attempting to download: '"+videomp4.title+".mp4'")
        try:
            videomp4.download()
            os.system("clear")
        except:
            print("An error has occurred")
            flag=True
        if flag==False:
            print("Download is completed successfully")


while True:
    os.system("clear")
    link = input("Enter the YouTube video URL: ")
    Download(link)
    answer=str(input("\nDo you wanna download other file?\n"))
    if answer=='nope' or answer=='no' or answer=='NO' or answer=='Nope':
        break;
    os.system("clear")



input("Have a nice day!")
