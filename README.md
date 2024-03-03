# youtube-downloader
This is a python script which dowload youtube video as mp3 or mp4


------------
DISCLAIMER
------------
This script is only for educational purpose, downloading YouTube video is AGAINST copyright and YouTube's terms. I do not take any responsibility for your usage.

-----------
ATTENTION
-----------
This script is usable with python 3.9.x 
If you have a newer version you can use pyenv to create a python venv with older pythons's versions


------------
FOR LINUX (ubunut debian based, for everyone else you need to change the package manager name)
1) You need to install python3 (sudo apt install python3) and python 3 pip (sudo apt install python3-pip) and install python venv (sudo apt install python3-venv)

2) Now you should create a dyrectory which will have the python script directory, the venv directory (python virtual environment which we will create after) and the pytube library directory

3) Now you need to create the virtual environment for python (python3 -m venv "put here the dyrectory location")

4) Now you need to git clone the pytube library code in its directory (git clone https://github.com/pytube/pytube.git)

5) Now you need to activate the python virtual  environment (source "put here the venv directory location"/bin/activate)

6) Now you need to install the pytube library on the python venv, go with your terminal in the pytube directory and use the command "python3 -m pip install ."

7) Now you are ready to execute the python script, go with you terminal in the python script directory and execute it (python3 main.py)


------------
FOR WINDOWS
1) You have to install python 3, you can install it by the microsoft store
1) You need to install pytube and pydub, open the cmd as administrator and put the command "pip install pytube pydube"
2) Now download the main.py file for the repository and you are ready to execute the python script
------------
