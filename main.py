import sys, os, time, webbrowser, urllib.request, zipfile, io, subprocess
from shutil import copyfile
import shutil
from  zipfile import ZipFile
from files import *
from com import *
from excom import *
start_path = os.getcwd()
def Run():

    def fallback():
        print('command doesnt exist')

    def checkDirectory():
        cd = input('cd~dir.check$ ')
        if os.path.exists(cd):
            print(os.path.exists(cd))
        else:
            print('that directory does not exist')

    # create a dictionary that maps input strings to functions (notice that the functions are only named, not executed)
    # that way, the main loop doesn't have to check against multiple strings to try and match one to the user's input
    # this is easier to maintain, and faster too!
    # I've done 3 of your commands as an example of what I mean
    actionDictionary = {
        'cd.dwn': download,
        'cd.rd': read,
        'cd~dir': checkDirectory
    }


    while True:
        start = input('>')
        # get reference for which function to execute, then execute it
        actionToRun = actionDictionary.get(start, fallback)
        actionToRun()
        
        # if start == 'cd.dwn':
        #     download()
        # elif start == 'cd.rd':
        #     read()
        # elif start == 'cd@': ## Not acctive in final version ~~ Results in shutdown
        #     filename = input('cd@ ')
        #     fd = os.open(filename, os.O_RDWR)
        #     print("File size (in bytes): " + str(os.stat(fd).st_size))
        #     length = 72
        #     os.ftruncate(fd, length)
        # elif start == 'cd.home' or start == 'cd!':
        #     os.chdir(start_path)
        # elif start == 'cd~dir':
        #     cd = input('cd~dir.check$ ')
        #     if os.path.exists(cd):
        #         print(os.path.exists(cd))
        #     else:
        #         print('that directory does not exist')
        # elif start == 'cd~':
        #     path = os.getcwd()
        #     print(path)
        # elif start == 'wd':
        #     path = input('wd.path$ ')
        #     print(path)
        #     os.chdir(path)
        # elif start == 'clear':
        #     os.system('cls' if os.name == 'nt' else 'clear')
        # elif start == 'ver':
        #     print('Version 0.04.34')
        # elif start == 'ls':
        #     print(os.listdir(os.getcwd()))
        # elif start == 'cd.wr':
        #     write()
        # elif start == 'cd.ex':
        #     extra()
        # elif start == 'cd.ex.com':
        #     run_ex()
        # elif start == 'cd.com':
        #     command()
        # elif start == 'quit':
        #     break
        # elif start == 'cd.ex.opt':
        #     ext_com()
        # else:
        #     print('command doesnt exist')
    return
Run()