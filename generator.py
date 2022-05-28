def my_range(first=1, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


my_range()

ranger = my_range(1, 5)
print(ranger)
for x in ranger:
    print(x)

# for try_agein in range:
#     print(try_agein)  # не сработает, генератор истощился

# неявное выполнение yield - включения генераторов

gener = (pair for pair in zip(['a', 'b'], ['1', '2']))
print(gener)


def document_it(func):
    def new_function(*args, **kwargs):
        print("running function:", func.__name__)
        print("positional arguments:", args)
        print('keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print("result:", result)
        return result

    return new_function


def add_ints(a, b):
    return a + b


add_ints(3, 5)
