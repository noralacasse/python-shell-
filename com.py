import os

def ext_com():
    while True:
        a = input('cd.ext.com// ')
        if a == 'shutdown' or a == 'sd':
            check = input('do you want to shut down ? [y/n]: ')
            if check == 'n':
                break
            elif check == 'y':
                os.system("shutdown /s /t 1")
        elif a == 'restart' or a == 'rt':
            check = input('do you want to reastart your computer? [y/n]: ')
            if check == 'n':
                break
            elif check == 'y':
                os.system('shutdown /s /t 1')
        elif a == 'back':
            break
        elif a == 'run':
            filename = input('cd.ext.com.file.exe// ')
            os.system(filename)
        else:
            print('that is not a command')
    return
def command():
    while True: 
        command = input('cd.com/')
        if command == 'back':
            break
        os.system(command)
    return