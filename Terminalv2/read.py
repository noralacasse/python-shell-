from zipfile import ZipFile
def read():
    def unless():
        print('That command does not exist')
    def read_file():
        read_in = input('read# ')
        f = open(read_in, 'r')
        print(f.read())
    def read_echo():
        read_in = input('echo# ')
        f = open(read_in, 'r')
        print(f.read())
        f.close()
        with open(read_in, 'w'): pass
    def read_zip():
        read_in = input('zip% ')
        with ZipFile(read_in, 'r') as zf:
            zip_Read = input('zip.file% ')
            with zf.open(zip_Read) as zfile:
                print(zfile.read())
    readDictionary = {
        'read': read_file,
        'echo': read_echo,
        'rd.zip': read_zip
    }
    while True:
        read_action = input('cd.rd/ ')
        if read_action == 'back':
            break
        readDo = readDictionary.get(read_action, unless)
        readDo()
    return