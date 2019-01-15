# use recursion to determine if a string is a palindrome


def is_palindrome(s):

    for i in range(len(s)):
        if s[i] != s[len(s) - 1 - i]:
            return False

    return True


def palindrome_recursion(n, s):
    pass