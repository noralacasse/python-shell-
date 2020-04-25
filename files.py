import sys, os, time, webbrowser, urllib.request, zipfile, io, subprocess
from shutil import copyfile
import shutil
from  zipfile import ZipFile

def download():
    while True: 
        down_action = input('download> ')
        if down_action == 'brw':
            site = input("website> ")
            webbrowser.open(site)
        elif down_action == 'dod':
            print('Beginning file download with cross os...')
            url = input('Url> ')
            dirc = input('Directory> ')
            urllib.request.urlretrieve(url, dirc)
        elif down_action == 'back':
            break
        else:
            print('command does not exist ')
    return

def read():
    while True:
        read_ac = input('read action # ')
        read_in = input('read file # ')
        if read_ac == 'rf.read':
            f = open(read_in, 'r')
            print(f.read())
        elif read_ac == 'rf.zip':
            with ZipFile(read_in) as zf:
                next_ac = input('rf.zip.read$ ')
                if next_ac == '.file':
                    next_file = input('rf.zip.read.file$ ')
                    with zf.open(next_file):
                        print('rf.zip.read.file/%s$ '%next_file + next_file.read())
        elif read_ac == 'rf.echo':
            print('echo %s' %read_in)
            f =open(read_in, 'r')
            print(f.read())
            f.close()
            with open(read_in, 'w'): pass
        elif read_ac == 'back':
            break
        else:
            print('command does not exist')
    return

def extra():
    while True:
        action_in = input('ex.action# ')
        if action_in == 'ex.delete':
            file_del = input('file> ')
            os.remove(file_del)
            print('File has been deleted')
        elif action_in == 'ex.copy':
            src = input('source> ')
            dst = input('Copy to> ')
            copyfile(src, dst)
            print('Finished...')
        elif action_in == 'ex.move':
            in_file = input('File> ')
            src = in_file
            des = input('Move> ')
            dest = shutil.move(src, des)
            print('%s moved to %s' %in_file %des)
            break
        elif action_in == 'ex.mk':
            filename = input('ex.mk.new> ')
            f = open(filename, 'w+')
        elif action_in == 'back':
            break
        else:
            print('that command doesnt exist')
    return

def write():
    while True: 
        write_ac = input('write action$ ')
        write_in = input('write to$ ')
        if write_ac == 'wf.wr':
            write_wr = input('write to %s> '%write_in)
            f = open(write_in, 'w')
            f.write(write_wr)
            f.close()
        elif write_ac == 'wf.to':
            print('touch %s' %write_in)
            with open(write_in, 'w'): pass
            f = open(write_in, 'w')
            Touch_to = input('touch>> ')
            f.write(Touch_to)
        elif write_ac == 'back':
            break
        elif write_ac == 'wf.ap':
            f = open(write_in, 'a')
            append_in = input('appending to %s> ' %write_in)
            f.write(append_in)
            f.close()
        else: 
            print('command does not exist')
    return
