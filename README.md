# Youtube Downloader ![Youtube](https://cms.autocarpro.in/images/youtube-logo.png)
![Python 3.8.10=>](https://img.shields.io/badge/Python-3.8.10%3E-green)
![Python3.9.x](https://img.shields.io/badge/Python-3.9.X-green)
![Python3.10.x](https://img.shields.io/badge/Python-3.10.x-green)
![python 3.11.x](https://img.shields.io/badge/Python-3.11.x-green)

![Phyton 3.8.9<](https://img.shields.io/badge/Python-3.8.9%3C-red)
![python 3.12.x](https://img.shields.io/badge/Python-3.12.x-orange)


This is a python script which download youtube video and playlsit as mp3 or mp4

------------
**DISCLAIMER:**
This script is only for **educational purpose**, downloading YouTube video is **AGAINST** copyright and YouTube's terms. **The autor of this tool do not take any responsibility** for your usage.


------------
## INSTALLATION ⚙️
1. Install python (preferably one of the indicated versions) if your systemn does not already have python

2. Download or clone the repository:

    `git clone https://github.com/En7ity303/youtube-downloader.git`

3. Install the requirements:

    `pip3 install -r requirements.txt`

4. You are ready to use the program


-----------
## USAGE 🔧
This script is surely usable with the elencated versions of Python which i have tested on my own, if you have a different version of python you can try to use the tool but it may not function properly 

-----------
The starting interface of the program allow you to choose some settings, the fisrt one allow you to choose the path where to download the file, the second one let you see the current download path wich is by default setted to '.' which means the files are going to be dowloaded in the same folder in which is located the programm, the tird option starts the program
<p align="center">
<img align="center" src="img/img1.png" width="600">
</p>

After you have started the program you can choose to download a video or a playlist
<p align="center">
<img align="center" src="img/img2.png" width="600">
</p>


After you have insert the url you can choose the format you wanna download the files into:
<p align="center">
<img align="center" src="img/img3.png" width="600">
</p>

-----------
## TASK LIST
### JUST DID IT
- [x] Allow to choose the format
- [x] Allow to choose the path of the downloads
- [x] Allow to choose from basic resolution
- [x] In application mp4 to mp3 convertion
### TO DO
- [ ] Allow to choose the specific resolution for each video
- [ ] Add a reset button for all the settings
- [ ] Improve the code for choosing the commands

-----------
## ATTENTION ⚠️🚨
Now there is a problem with pytube 15.0.0 I sugest to momentary use older versions of pytube such as 12.1.3 trought this command:

`pip3 install pytube==12.1.3`

if you really want to use the version 15.0.0 you must follow this guide https://github.com/pytube/pytube/issues/1712

## ATTENTION ⚠️🚨
Now there is an issue with python 3.12.X on macOS system so if you have a macOS device you must use 3.11.8 or above 
