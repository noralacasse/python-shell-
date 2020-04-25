import os, sys

def run_ex():
    while True:
        in_action = input('ex/com/action/ ')
        if in_action == 'lg':
            print(os.getlogin())
        elif in_action == 'pd':
            print(os.getpid())
        elif in_action == 'de':
            print(os.device_encoding(10))
        elif in_action == 'back':
            break
        else:
            print('command doesnt exist')
    return