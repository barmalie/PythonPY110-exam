from datetime import datetime


# декораторы

def timeit(arg):
    print(arg)

    def outer(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result

        return wrapper

    return outer


@timeit('name')
def one(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l


@timeit('name')
def two(n):
    l = [x for x in range(n) if x % 2 == 0]
    return l


l1 = timeit('name')(one)(10)

one(10)

'''
name
name
name
0:00:00
0:00:00
0:00:000
'''
