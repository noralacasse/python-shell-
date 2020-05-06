
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

    def workingDirectory():
        path = input('wd.path$ ')
        os.chdir(path)
        print(os.getcwd())

    def non_ess():
        def time():
            import datetime
            now = datetime.datetime.now()
            print('Currnet date and time: ')
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
        def ver():
            print('version 0.04.5')
        Action2Dictionary = {
            'ver': ver,
            'time': time
        }
        action = input('non_ess action: ')
        Non_essAction = Action2Dictionary.get(action, fallback)
        Non_essAction()

    def ess():
        def ls():
            print(os.listdir(os.getcwd()))

        def home():
            os.chdir(start_path)

        EssDictionary = {
            'ls': ls,
            'cd!':home
        }
        ess_action = input('ess action: ')
        Ess_action= EssDictionary.get(ess_action, fallback)
        Ess_action()

    def checkDir():
        print(os.getcwd())

    def clear():
        os.system('cls' if os.name=='nt' else 'clear')

    actionDictionary = {
        'cd.dwn': download,
        'cd.rd': read,
        'cd.wr': write,
        'cd.ex': extra,
        'cd.ex.com':run_ex,
        'cd.com': command,
        'cd~dir': checkDirectory,
        'cd~': checkDir,
        'wd': workingDirectory,
        'cd.ex.opt': ext_com,
        'clear': clear,
        'non_ess': non_ess,
        'ess': ess
    }


    while True:
        start = input('>')
        if start == 'quit' or start == 'exit':
            break
        actionToRun = actionDictionary.get(start, fallback)
        actionToRun()
    return
Run()