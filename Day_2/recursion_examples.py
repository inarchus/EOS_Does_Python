
def factorial_iterative(n: int):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def factorial_recursive(n: int):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def fibonacci_iterative(n):
    f_1 = 1
    f_2 = 1

    for i in range(2, n):
        if i % 2:
            f_1 += f_2
        else:
            f_2 += f_1

    return max(f_1, f_2)


def fibonacci_recursive(n):
    if n < 3:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


fibonacci_list = [1, 1, 1]


def fibonacci_dynamic(n):
    global fibonacci_list

    if len(fibonacci_list) < n:
        fibonacci_dynamic(n - 1)

    if len(fibonacci_list) <= n:
        fibonacci_list.append(fibonacci_list[n - 1] + fibonacci_list[n - 2])

    return fibonacci_list[n]


print(*[fibonacci_iterative(i) for i in range(20)])
print(*[fibonacci_recursive(i) for i in range(20)])
print(*[fibonacci_dynamic(i) for i in range(20)])

for i in range(50):
    print(i, fibonacci_iterative(i))
