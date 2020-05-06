import os, sys, datetime
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def ls():
    print(os.listdir(os.getcwd()))

def command():
    while True:
        commands = input('cd.com/')
        if commands == 'back':
            break
    return
def time():
    print(datetime.datetime.now())
def shutdown():
    check = input('do you want to shut down? [y/n]')
    if check == 'y':
        os.system("shutdown /s /t 1")
    else:
        return