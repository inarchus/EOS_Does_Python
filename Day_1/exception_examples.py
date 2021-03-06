def try_except_else():
    try:
        x = int(input('Enter an integer:'))
    except ValueError:
        print('you did not enter an integer')
    else:
        print(x, 'is an integer')


def try_except_finally():
    try:
        s = input('Enter an integer:')
        x = int(s)
    except ValueError:
        print('you did not enter an integer')
    else:
        print(x, 'is an integer')
    finally:
        print(s, 'was entered')
        # caution, may fail
        print(x, 'was entered')


def except_as():
    try:
        f = open('file_that_doesnt_exist.nope', 'r')
    except OSError as the_error:
        print(the_error)
    else:
        f.close()


class EOSError(Exception):
    def __init__(self, message='Some Kind of FOT Error'):
        self.message = message


def i_am_a_problem():
    raise EOSError('I couldn\'t load a wotis! Or something else that is bad!')


def ready_to_cause_trouble():
    try:
        i_am_a_problem()
    #except EOSError as e:
    #    print(e.message)
    except IOError:
        print('hi')
    else:
        print('no problem my dudes')


class BlahObject:
    def __init__(self, blah):
        self.blah=blah

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.blah = 0


def with_examples():
    with open('first_file.txt', 'r') as f:
        for line in f:
            print(line.strip())

    if False:
        with open('definitely_doesnt_exist.txt', 'r') as f:
            for line in f:
                print(line)

    with BlahObject(3) as f, BlahObject(5) as g:
        print(f.blah, g.blah)

    print(f.blah, g.blah)



# try_except_else()
# try_except_finally()
# except_as()
# ready_to_cause_trouble()
with_examples()

