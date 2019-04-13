import random


def first_example():
    def f_1(x):
        return x * x

    def f_2(x):
        return 3 * x + 1

    def f_3(x):
        return (pow(2, x) - 17) % pow(12, 3)

    list_of_functions = [f_1, f_2, f_3]
    list_of_inputs = [random.randint(0, 100) for _ in range(10)]

    print(list_of_functions)
    print(list_of_inputs)

    for f in list_of_functions:
        list_of_outputs = []
        for x in list_of_inputs:
            list_of_outputs.append(f(x))
        print(f.__name__, list_of_outputs)


first_example()

def second_example():
    method = 'rsa'
    the_file = ''

    def encrypt_and_process(file, hash_method):
        pass

    def mda5(s):
        pass

    def sha1(s):
        pass

    def rsa2048(s):
        pass

    hashing_functions = {'mda5': mda5, 'sha1': sha1, 'rsa': rsa2048}

    encrypt_and_process(the_file, hashing_functions[method])
