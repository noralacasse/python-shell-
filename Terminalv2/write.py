def write():
    def unless():
        print('that command doesnt exist')
    def write_file():
        write_in = input('filename> ')
        write_wr = input('write to %s> '%write_in)
        f = open(write_in, 'w')
        f.write(write_wr)
        f.close()
    def append_file():
        write_in = input('filename> ')
        append_in = input('appending to %s> ' %write_in)
        f = open(write_in, 'a')
        f.write(append_in)
        f.close()
    def touch_file():
        write_in = input('filename> ')
        print('touch %s' %write_in)
        tocuh_in = input('touch %s> ' %write_in)
        with open(write_in, 'w'): pass
        f = open(write_in, 'w')
        f.write(tocuh_in)
        f.close()
    writeDictionary = {
        'write': write_file,
        'touch': touch_file,
        'append': append_file
    }
    while True:
        write_action = input('write$ ')
        if write_action == 'back':
            break
        action = writeDictionary.get(write_action, unless)
        action()
    return

