## Imports
import urllib.request, datetime, os
from mcom import *
from download import *
from rd import *
from file_utilities import *
from write import *
from read import *
## Main Function

home = os.getcwd()
start_time = datetime.datetime.now()
def read_StartTime():
    print(start_time)

def go_Home():
    os.chdir(home)
    print(os.getcwd)

def Run():
    def fallback():
        print('command doesnt exsist')

    actionDictionary = {
        'clear': clear,
        'ls': ls,
        'cd.com': command,
        'power': shutdown,
        'lg': lg,
        'see_path': see_Path,
        'download': downlaod,
        'brw': browse,
        'cd.rd': read,
        'cd!': go_Home,
        'st': read_StartTime,
        'del': delete,
        'ex.move': move,
        'ex.copy': copy,
        'ex.mk': make,
        'size': size,
        'cd.wr': write
    }

    while True:
        start = input('>')
        if start == 'quit' or start == 'exit':
            break
        action = actionDictionary.get(start, fallback)
        action()

def start_up():
    def get_Up(host='http://google.com'):
        try:
            urllib.request.urlopen(host)
            return True
        except Exception as e:
            print(e)
            return False
    
    print('connected' if get_Up() else 'Some functions may not work as you are not connected to the interned')
    Run()

start_up()