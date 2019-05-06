
def read_wotis(file_name):
    wotis_file = open(file_name)

    for line in wotis_file:
        print(line)

    wotis_file.close()


if __name__ == '__main__':
    file_name = input('Enter the name of the file: ')
    read_wotis(file_name)
