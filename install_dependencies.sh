#!/bin/bash

#For Windows 10 enable windows subsystem for linux and download Ubuntu from the windows store
#https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/

#On Windows 10 navigate to the directory of the script and run bash -c "sh insall_dependencies.sh" (Make sure you have pip installed on your machine)

python -m pip install pymongo
python -m pip install dnspython
python -m pip install graphene
python -m pip install Flask
python -m pip install Flask_Pymongo