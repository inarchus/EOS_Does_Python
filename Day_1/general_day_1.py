import math
import random
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import datetime as dt
import string
import gc

def message_boxes():
    messagebox.showinfo('This is the title.', 'This is the Message')
    messagebox.showwarning('This is the title.', 'This is the Message')
    messagebox.showerror('This is the title.', 'This is the Message')
    messagebox.askokcancel('MessageBox', 'Is it ok, or should we cancel?')
    messagebox.askyesno('MessageBox', 'Yes, or no? (YN)')
    messagebox.askquestion('MessageBox', 'Yes, or no? (Q)')
    messagebox.askretrycancel('MessageBox', 'Retry or Cancel')
    messagebox.askyesnocancel('MessageBox', 'More Options')


def taylor(x, n, *c_array):
    """
        nested function example
    """

    def factorial(n):
        """
            takes n and returns n!
        """
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    result = 0
    for i, c in enumerate(c_array):
        if i <= n:
            result += c * pow(x, i) / factorial(i)

    return result


# print(taylor(0.5, 100, *[pow(1/2, i) for i in range(100)]))

def card_deck_example():

    # this is the setup
    spade = '\u2660'
    club = '\u2663'
    heart = '\u2664'
    diamond = '\u2662'

    suits = ['\u2660', '\u2663', '\u2664', '\u2662']
    types = [str(x) for x in range(2, 11)] + ['J', 'Q', 'K', 'A']
    card_order = [x + y for x in suits for y in types]
    # here is the example
    card_map = {card: pos for pos, card in enumerate(card_order)}

    print(card_map[club+'3'])

    print(card_map)

# for i, thing in enumerate(['a', 'b', 'c', 'd', 'e']):
#     print(i, thing)

def pass_by_value():
    def modify_value(x):
        x += 2
        print('locally', x)

    x = 4
    modify_value(x)
    print(x)


def pass_by_reference():
    def modify_list(the_list):
        the_list.extend([1, 2, 3])
        print('locally', the_list)

    L = ['a', 17, '3', 'hello', {'a': 1}]
    modify_list(L)
    print(L)

    def modify_dictionary(the_dict):
        the_dict['happy'] = 'the turtles'
        the_dict['black hole'] = 'Suskind'
        print('locally', the_dict)

    D = {'Stern': 'Gerlach', 'Michelson': 'Morley', 'Rosen': 'Podolsky'}
    modify_dictionary(D)
    print(D)


def palindrome_check(s):

    p = True

    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            p = False

    if p:  # p == True
        print(s, 'is a palindrome')
    else:
        print(s, 'is not a palindrome')


# palindrome_check('racecar')

def splatty():

    def sigma_2(*x):
        s = 0
        for i in range(len(x)):
            for j in range(i + 1, len(x)):
                s += x[i]*x[j]
        return s

    L = [random.randint(0, 10) for _ in range(10)]
    print(sigma_2(*L))
    print(*L)


def list_stuff():

    L1 = [random.randint(0, 1000) for _ in range(8)]
    L2 = [random.randint(0, 1000) for _ in range(5)]
    print(L1, L2)
    L1 += L2
    print(L1)

    L3 = [random.randint(0, 100) for _ in range(10)]
    print(L3)
    del L3[3]
    print(L3)

    L4 = [i + 1 for i in range(10)]
    print(L4)
    L4.remove(7)
    print(L4)

    L5 = [14 for _ in range(10)]
    find = L5[3]
    i = L5.index(17)
    print(find, i, L5)


def length_and_string():
    s = 'hello, I am a string, and this has a length'
    print(len(s))
    L = [random.randint(0, 1000) for _ in range(random.randint(1, 10000))]
    print(len(L))

    hello_string = 'hello'
    for char in hello_string:
        print(char)


def enumerate_example():
    
    L = [random.choice(string.ascii_lowercase) for _ in range(10)]
    print(L)
    for i, c in enumerate(L):
        print('the', i, 'th', 'letter is', c)
        
    L = [(random.randint(0, 10), random.choice(string.ascii_lowercase)) for _ in range(10)]
    print(L)
    for i, x, y in enumerate(L):
        print(i, x, y)

    
def pass_the_nop():
    """
        pass is the python nop, which is necessary because of the white space sensitivity.
    """

    for i in range(100):
        pass

    f = open('first_file.txt', 'r')
    while f.readline():
        pass

    x = 3; y = 2
    if x < y:
        pass

    try:
        pass
    except IOError:
        pass

    def fun_with_functions(alpha, beta):
        pass

        r = alpha
        s = beta

    fun_with_functions(3, 2)


def calling_named_arguments():

    def call_me(name, number, message, **kwargs):
        print(*list((x, kwargs[x]) for x in kwargs))
        print(name, number, message)

    call_me(name='Eric', number='555-444-3333', message='you know I love Python',
            payment=20, upbraidment=3, strength=1, charisma=17)
    call_me(payment=15, name='Ru', message='Got Beef', number='777-888-7788')


def scope():
    s = 17

    def sub_function(x, y):
        r = x | y + 1
        v = r & y - 1 + s
        # print(vars(), globals())
        return v ** 2

    t = sub_function(13, 19)
    print(t)
    # print(vars())


def upper_and_lower_egypt():
    s1 = 'hat'
    s2 = 'HAT'
    k1 = 'This is a mixed string; With all kinds of & symbols and || things.  '
    print(k1.upper())
    print(s2.lower())

    if s1 == s2:
        print('they are the same')
    elif s1.upper() == s2.upper():
        print('they are essentially the same, modulo case')


# pass_the_nop()
# length_and_string()
# enumerate_example()
# calling_named_arguments()
# scope()
upper_and_lower_egypt()
