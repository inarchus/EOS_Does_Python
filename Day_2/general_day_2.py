import random


def sort_vs_sorted():
    L = [random.randint(0, 100) for _ in range(10)]
    L.sort()
    print(L)

    L2 = [random.randint(0, 100) for _ in range(10)]
    L3 = sorted(L2)
    print(L2, L3)

    games = [('civ2', 19.99), ('star citizen', 80.00), ('Portal 2', 15), ('starcraft', 5)]
    games.sort(key=lambda x: x[1])
    print(games)


class SomeError(Exception):
    pass

def try_try_and_try_again():
    try:
        pass
    except ValueError:
        pass
    except IOError:
        pass
    except IndexError:
        pass
    else:
        print('no errors occurred')
    finally:
        print('doing this last, regardless of what happened')

    random_condition = False

    try:
        print('The majority of your code is here')
        print('Somewhere in here, we raise ')
        if not random_condition:
            raise SomeError
        print('Probably more code here too.  ')
        # Here we don\'t want this code to execute if random_condition is False.
        # It will cause problems down the road
    except SomeError:
        print('Some error has occurred.')


def try_convert():
    stop = False
    while not stop:
        s = input('Enter an integer: ')
        try:
            x = int(s)
            stop = True
        except ValueError:
            print(s, 'cannot be converted.')

    print(x, 'is an integer')


def check_convert():

    digits = list(str(x) for x in range(0, 10))
    while True:
        s = input('Enter an integer: ')
        if all(c in digits for c in s):
            x = int(s)
            break
        else:
            print(s, 'cannot be converted.')

    print(x, 'is an integer')


def file_error():
    the_file = None
    try:
        the_file = open('sample.txt', 'r')
    except IOError:
        print('sample.txt', 'could not be opened')
    finally:
        print('we do this right before leaving try block')

    return the_file


def more_sorting():
    pass


def lbyl_vs_eapf():
    pass


def lambda_stuff():
    # lambda_list = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(100)]
    # map(lambda x, y: (x ** 2) * (y ** 3) + x * y + 1, lambda_list)
    L = [random.randint(0, 100) for _ in range(10)]
    list(map(lambda x: print('x is', x), L))
    print(L)
    print(list(map(lambda x: x if x % 2 else 0, L)))

    def f(x, y):
        return (x ** 2) * (y ** 3) + x * y + 1

    f(3, 2)
    #arguments = [random.randint(0, 100) for _ in range(10)]

    #def do_something_to(*args):
    #    return sum(args)

    #(lambda *args: do_something_to(args))(arguments)

    print((lambda x: x if x % 2 else 0)(16))
    print((lambda x: x if x % 2 else 0)(3))

    iterable = iter()
    def func():
        pass

    map(func, iterable)

    print((lambda x: x * x)(3))
    print((lambda x: x * x)(17))


# file_error()
# try_try_and_try_again()
# try_convert()
# check_convert()
# more_sorting()
lambda_stuff()
