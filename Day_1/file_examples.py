
def file_operations():
    # if you run this, you'll have to redownload the file
    # first_file = open('first_file.txt', 'wb')
    # first_file.write()
    # first_file = open('first_file.txt', 'w+')

    first_file = open('first_file.txt', 'r+')
    print(first_file.readlines())
    first_file.close()

    first_file = open('first_file.txt', 'a+')
    print(first_file.readlines())
    first_file.close()

    def file_ops():
        try:
            f = open('blah.txt', 'r')
            # really this means do something with the file
            print(f.readlines())
        except IOError:
            print('The file was unable to be opened')
        else:
            f.close()

    # file_ops()


def read_vs_read_vs_read():
    try:
        f = open('first_file.txt', 'r')
        line = f.readline().strip()
        while line:
            print(line)
            line = f.readline().strip()
    except OSError as e:
        print(e)
    else:
        f.close()

    try:
        f = open('first_file.txt', 'r')
        all_the_lines = f.readlines()
        for line in all_the_lines:
            print(line.strip())
    except OSError as e:
        print(e)
    else:
        f.close()

    try:
        f = open('first_file.txt', 'r')
        for line in f:
            print(line.strip())

    except OSError as e:
        print(e)
    else:
        f.close()


def writing_files():
    try:
        # doesn't matter what it is as long as it isn't empty
        s = 'a'
        f = open('write_experiment.txt', 'w')
        while s != '':
            s = input('Enter another line: ')
            f.write(s + '\n')
    except OSError as e:
        print(e)
    else:
        f.close()

# file_operations()
# read_vs_read_vs_read()
# writing_files()