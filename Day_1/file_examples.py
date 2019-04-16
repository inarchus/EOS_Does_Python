
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


file_operations()