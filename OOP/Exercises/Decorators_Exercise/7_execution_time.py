from time import time as tm


def exec_time(func):
    def wrapper(*args, **kwargs):
        t0 = tm()
        func(*args, **kwargs)
        t1 = tm()
        return t1 - t0
    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))