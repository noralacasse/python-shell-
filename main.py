import sys, os, time, webbrowser, urllib.request, zipfile, io, subprocess
from shutil import copyfile
import shutil
from  zipfile import ZipFile
from files import *
from com import *
from excom import *
start_path = os.getcwd()
def Run():
    while True:
        start = input('>')
        if start == 'cd.dwn':
            download()
        elif start == 'cd.rd':
            read()
        elif start == 'cd@': ## Not acctive in final version ~~ Results in shutdown
            filename = input('cd@ ')
            fd = os.open(filename, os.O_RDWR)
            print("File size (in bytes): " + str(os.stat(fd).st_size))
            length = 72
            os.ftruncate(fd, length)
        elif start == 'cd.home' or start == 'cd!':
            os.chdir(start_path)
        elif start == 'cd~dir':
            cd = input('cd~dir.check$ ')
            if os.path.exists(cd):
                print(os.path.exists(cd))
            else:
                print('that directory does not exist')
        elif start == 'cd~':
            path = os.getcwd()
            print(path)
        elif start == 'wd':
            path = input('wd.path$ ')
            print(path)
            os.chdir(path)
        elif start == 'clear':
            os.system('cls' if os.name == 'nt' else 'clear')
        elif start == 'ver':
            print('Version 0.04.34')
        elif start == 'ls':
            print(os.listdir(os.getcwd()))
        elif start == 'cd.wr':
            write()
        elif start == 'cd.ex':
            extra()
        elif start == 'cd.ex.com':
            run_ex()
        elif start == 'quit':
            break
        elif start == 'cd.ex.opt':
            ext_com()
        else:
            print('command doesnt exist')
    return
Run()