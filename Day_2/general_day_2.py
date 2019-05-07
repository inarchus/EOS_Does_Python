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


def mapping_examples():
    def square(x):
        return x * x

    L = [random.randint(0, 100) for _ in range(10)]
    L2 = list(map(square, L))
    L2A = list(map(lambda x: x*x, L))
    print(L)
    print(L2)
    print(L2A)

    list_of_floats = [32.123213, 21.8489456, 17.64643123123, 15.15484654]
    rounded_floats = list(map(lambda x: round(x, 2), list_of_floats))
    print(rounded_floats)

    list_of_string_numbers = ['32', '79', '121', '577', '281', '83']
    output_list = list(map(int, list_of_string_numbers))
    print(list_of_string_numbers)
    print(output_list)

    # list_of_lambdas.append(lambda x: (x, i))
    list_of_lambdas = []
    for i in range(10):
        list_of_lambdas.append(lambda x, k=i: (x, k))

    output_list = []
    for j in range(10):
        output_list.append(list_of_lambdas[j](j))

    print(output_list)


def multiple_return_values():
    
    def do_something(x, y):
        return x + y, x * y, x ** y, y ** x, x % y
    
    def messy(x, y, z):
        if z % 2:
            return x + y, x * y
        else:
            return x ** y, y ** x, x ^ y
    
    t = do_something(2, 7)
    print(t)
    
    the_sum, product, first_exp, other_exp, modded = do_something(7, 39)
    print(the_sum, product, first_exp, other_exp, modded)
    
    x_1, y_1 = messy(1, 2, 3)
    x_2, y_2, z_2 = messy(4, 5, 6)
    print(x_1, x_2, y_2, z_2)
    x_3, y_3 = messy(4, 5, 8)
    print(x_3, y_3)
    
    def good_and_evil():
        return 'good', 'evil'
    
    keep_the_good, _ = good_and_evil()

    list_brackets = []
    list_constructor = list()

    list_brackets.append(3)
    list_constructor.append(17)
    
# file_error()
# try_try_and_try_again()
# try_convert()
# check_convert()
# more_sorting()
# lambda_stuff()
# mapping_examples()
multiple_return_values()
