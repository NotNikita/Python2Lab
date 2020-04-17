import random


def cached(function):
    memo = {}  # like memory

    def wrapper(*args, **kwargs):
        # key - input
        # result - output
        key = args
        if kwargs:
            for item in sorted(kwargs.items()): #sorted оебспечивает устойчивость
                key += item

        # ==
        if key in memo:
            result = memo[key]
        else:
            result = function(*args, **kwargs)
            memo[key] = result

        return result

    return wrapper


@cached
def func(*args, **kwargs):
    out_arr = []  # output dictionary
    temp_arr = []  # for kwargs

    # args
    if args.__len__() != 0:# если args вообще был передан
        for n in args:
            out_arr.append(random.randint(1, 100) * n)

    # kwargs
    if kwargs.__len__() != 0:  # если kwargs вообще был передан
        for key in kwargs.keys():  # выписываем значения по ключам в список для вывода
            temp_arr.append(kwargs[key])

        for i in temp_arr:  # merging lists of arg and kwarg results
            out_arr.append(i)

    return out_arr


print("result: ", func(1, 2, 3) == func(1, 2, 3))  # позиционные аргументы
print("\n")
print("result: ", func(Hi=100, Me=200) == func(Hi=100, Me=200))
