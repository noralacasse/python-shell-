import os
import shutil
from shutil import copyfile
def delete():
    file_del = input('file> ')
    os.remove(file_del)
    print('File has been deleted')
def copy():
    src = input('source> ')
    dst = input('Copy to> ')
    copyfile(src, dst)
    print('Finished...')
def move():
    in_file = input('File> ')
    src = in_file
    des = input('Move> ')
    dest = shutil.move(src, des)
    print('%s moved to %s' %in_file %des)
def make():
    filename = input('ex.mk.new> ')
    f = open(filename, 'w+')
def size():
    filename = input('sz.file> ')
    try:
        file_size = os.path.getsize(filename)
    except OSError:
        print('Parh %s does not exsist or is inaccessible' %filename)
        return
    print('Size (in byte) of % s' %filename, file_size)
